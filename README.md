# PawPal+ AI Care Advisor

## Project Summary

PawPal+ AI Care Advisor is an applied AI system that extends the original PawPal+ pet care scheduler into a more intelligent and reliable pet-care assistant.

The original PawPal+ system helped pet owners manage daily routines such as feedings, walks, medications, grooming, and appointments. It used Python object-oriented programming with Owner, Pet, Task, and Scheduler classes to organize tasks, sort schedules, detect conflicts, and manage recurring care routines.

For Unit 9, I extended PawPal+ by adding a RAG-style AI Care Advisor. The new system retrieves relevant pet-care information from a structured knowledge base, generates a recommendation, assigns an urgency level, calculates a confidence score, and uses guardrails for emergency or low-confidence situations.

---

## Original Project Extended

**Original project:** PawPal+

**Original goal:** PawPal+ was originally designed as a smart pet care management system. It helped owners track pets, schedule care tasks, sort tasks by time, filter by pet or completion status, detect task conflicts, and support recurring daily or weekly tasks.

**How this project extends it:** The Unit 9 version keeps the original scheduling system and adds an AI-powered care advisor. This makes the system more useful because it not only organizes pet-care tasks, but also helps users reason about pet-care concerns using retrieval, confidence scoring, and safety guardrails.

---

## New AI Feature

### RAG-Style Care Advisor

The new AI feature is a small retrieval-augmented generation system.

When the user enters a pet-care concern, the system:

1. Validates the input  
2. Searches a pet-care knowledge base  
3. Retrieves the most relevant care topic  
4. Generates a recommendation grounded in the retrieved information  
5. Assigns an urgency level  
6. Calculates a confidence score  
7. Triggers guardrails for emergencies or unknown concerns  

This feature is fully integrated into the system through both the CLI (`ai_demo.py`) and the Streamlit app (`app.py`).

---

## Features

### Original PawPal+ Scheduling Features

- Add pets  
- Add care tasks  
- Generate today's schedule  
- Sort tasks by time  
- Filter tasks by pet  
- Filter tasks by completion status  
- Detect scheduling conflicts  
- Create recurring daily or weekly tasks  

### Unit 9 AI Extension Features

- RAG-style retrieval from a pet-care knowledge base  
- AI-generated care recommendations  
- Urgency levels: low, medium, high, unknown  
- Confidence scoring  
- Emergency guardrails  
- Safe fallback when the system does not have enough context  
- CLI demo with multiple example inputs  
- Automated tests for both scheduling and AI advisor behavior  

---

## System Architecture

The system consists of two main components:

### 1. Scheduling System
- `Owner`, `Pet`, `Task`, and `Scheduler`
- Handles structured pet care routines

### 2. AI Care Advisor
- `CareAdvisor`
- `CARE_KNOWLEDGE_BASE`
- Performs retrieval and generates grounded recommendations

### Data Flow

User → Streamlit UI → CareAdvisor → Knowledge Base → Response (urgency + confidence + recommendation)

---

## Demo Walkthrough

[Watch the demo video](https://drive.google.com/file/d/1BZmcGnuxndADRjMrweC8AUZClN0VMTpf/view?usp=sharing)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mishtigala19/ai110-module2show-pawpal-starter.git
cd ai110-module2show-pawpal-starter