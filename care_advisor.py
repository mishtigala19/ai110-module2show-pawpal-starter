from dataclasses import dataclass
from typing import Dict, List

from care_knowledge_base import CARE_KNOWLEDGE_BASE


@dataclass
class CareAdvice:
    query: str
    matched_topic: str
    recommendation: str
    urgency: str
    confidence: float
    sources_used: List[str]
    guardrail_triggered: bool


class CareAdvisor:
    """
    RAG-style pet care advisor.

    The advisor retrieves relevant care information from a small knowledge base,
    applies safety guardrails, calculates a confidence score, and generates a
    recommendation for the user.
    """

    def __init__(self, knowledge_base: List[Dict] = None):
        self.knowledge_base = knowledge_base or CARE_KNOWLEDGE_BASE

    def validate_query(self, query: str) -> str:
        """Clean and validate the user's pet-care question."""
        cleaned_query = query.strip().lower()

        if not cleaned_query:
            raise ValueError("Please enter a pet-care question or concern.")

        if len(cleaned_query) < 5:
            raise ValueError("Please provide a little more detail about the pet-care concern.")

        return cleaned_query

    def retrieve_relevant_entries(self, query: str) -> List[Dict]:
        """
        Retrieve knowledge base entries that match the user's query.

        This is a simple keyword-based retrieval system. It acts like a small RAG
        retriever because the final response is grounded in retrieved care entries.
        """
        cleaned_query = self.validate_query(query)
        matches = []

        for entry in self.knowledge_base:
            score = 0
            for keyword in entry["keywords"]:
                if keyword in cleaned_query:
                    score += 1

            if score > 0:
                entry_copy = entry.copy()
                entry_copy["score"] = score
                matches.append(entry_copy)

        matches.sort(key=lambda item: item["score"], reverse=True)
        return matches

    def calculate_confidence(self, matches: List[Dict]) -> float:
        """Calculate confidence based on how many keyword matches were found."""
        if not matches:
            return 0.25

        top_score = matches[0]["score"]

        if top_score >= 3:
            return 0.95
        if top_score == 2:
            return 0.85
        return 0.70

    def generate_advice(self, query: str) -> CareAdvice:
        """
        Generate a pet-care recommendation using retrieval, guardrails, and confidence scoring.
        """
        cleaned_query = self.validate_query(query)
        matches = self.retrieve_relevant_entries(cleaned_query)

        if not matches:
            return CareAdvice(
                query=query,
                matched_topic="unknown",
                recommendation=(
                    "I could not find a strong match in the PawPal+ care knowledge base. "
                    "Please monitor your pet and contact a veterinarian if symptoms continue or worsen."
                ),
                urgency="unknown",
                confidence=0.25,
                sources_used=[],
                guardrail_triggered=True,
            )

        top_match = matches[0]
        confidence = self.calculate_confidence(matches)
        guardrail_triggered = top_match["urgency"] == "high"

        if guardrail_triggered:
            recommendation = (
                f"{top_match['advice']} Because this concern may be urgent, "
                "please seek professional veterinary help immediately."
            )
        else:
            recommendation = (
                f"Based on the PawPal+ care knowledge base, this appears related to "
                f"{top_match['topic']}. {top_match['advice']}"
            )

        return CareAdvice(
            query=query,
            matched_topic=top_match["topic"],
            recommendation=recommendation,
            urgency=top_match["urgency"],
            confidence=confidence,
            sources_used=[top_match["topic"]],
            guardrail_triggered=guardrail_triggered,
        )

    def format_advice(self, advice: CareAdvice) -> str:
        """Format the advice object for CLI display."""
        return (
            f"Query: {advice.query}\n"
            f"Matched Topic: {advice.matched_topic}\n"
            f"Urgency: {advice.urgency}\n"
            f"Confidence: {advice.confidence:.2f}\n"
            f"Guardrail Triggered: {advice.guardrail_triggered}\n"
            f"Recommendation: {advice.recommendation}\n"
            f"Sources Used: {', '.join(advice.sources_used) if advice.sources_used else 'None'}"
        )