import pytest

from care_advisor import CareAdvisor


def test_advisor_retrieves_vomiting_advice():
    advisor = CareAdvisor()

    result = advisor.generate_advice("My dog is vomiting after breakfast.")

    assert result.matched_topic == "vomiting"
    assert result.urgency == "medium"
    assert result.confidence >= 0.70
    assert "vomiting" in result.recommendation.lower()


def test_advisor_triggers_emergency_guardrail():
    advisor = CareAdvisor()

    result = advisor.generate_advice("My dog cannot breathe and collapsed.")

    assert result.matched_topic == "emergency"
    assert result.urgency == "high"
    assert result.guardrail_triggered is True
    assert "emergency" in result.recommendation.lower() or "veterinarian" in result.recommendation.lower()


def test_advisor_handles_unknown_query_safely():
    advisor = CareAdvisor()

    result = advisor.generate_advice("My pet is acting strange in a way I cannot describe.")

    assert result.matched_topic == "unknown"
    assert result.confidence == 0.25
    assert result.guardrail_triggered is True
    assert "veterinarian" in result.recommendation.lower()


def test_advisor_rejects_empty_query():
    advisor = CareAdvisor()

    with pytest.raises(ValueError):
        advisor.generate_advice("")