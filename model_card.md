# Model Card: PawPal+ AI Care Advisor

## Base Project

This project extends **PawPal+**, which was originally a pet care scheduling system.

The original system allowed users to:
- Add pets
- Create tasks
- Generate schedules
- Sort and filter tasks
- Detect conflicts
- Handle recurring tasks

---

## What This AI System Does

The extended system adds an **AI Care Advisor**.

It allows users to input a pet-care concern and:

- Retrieves relevant information from a knowledge base
- Generates a recommendation
- Assigns an urgency level (low, medium, high)
- Calculates a confidence score
- Applies safety guardrails

---

## AI Technique Used

This system uses a **RAG-style (Retrieval-Augmented Generation) approach**:

1. User enters a query
2. System searches a knowledge base
3. Retrieves the most relevant entry
4. Generates a grounded response based on that entry

---

## Reliability Mechanisms

This system includes:

### 1. Input Validation
- Rejects empty or very short inputs

### 2. Retrieval-Based Responses
- Does not generate random answers
- Uses only knowledge base data

### 3. Confidence Scoring
- Based on keyword match strength

### 4. Guardrails
- Detects emergencies (e.g., cannot breathe, collapse)
- Provides safe fallback for unknown queries

---

## Example Guardrail Case

**Input:**