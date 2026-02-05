# Agentic Resume Screening – AI Prototype

This project is an AI-powered **prototype** that explores how Large Language Models (LLMs) can assist in resume screening by extracting structured information and comparing resumes with job descriptions.

The aim is to understand how AI can support **early-stage candidate evaluation**, not to build a production-ready system.

---

## Problem Overview
Resume screening is time-consuming when recruiters handle large numbers of applications.  
This prototype explores how AI can:
- Extract relevant details from resumes
- Compare candidate profiles with job requirements
- Generate a structured evaluation output

---

## Approach

### AI-Centric Design
- A Large Language Model (LLM) processes resume and job description text
- Prompts guide the model to extract skills, experience, and relevance
- Outputs are returned in a structured JSON format for clarity

### High-Level Flow
Resume PDF  
   ↓  
Text Extraction  
   ↓  
LLM-based Analysis  
   ↓  
Structured Evaluation Output (JSON)

---

## System Implementation (High-Level)
- FastAPI is used as a lightweight backend to expose the AI logic
- The backend mainly acts as a delivery layer between input and output
- The primary focus is on AI behavior and system flow, not backend depth

---

## Key Learnings
- How prompts influence structured outputs from Large Language Models (LLMs)
- Importance of clear input and output formats in AI systems
- How AI logic can be integrated into simple applications

---

## Limitations
- Output quality depends on the quality and format of resume text
- No large-scale evaluation or benchmarking was performed
- The system is not optimized for production use

---

## Technologies Used
- Python
- FastAPI
- Large Language Model (via API)
- JSON

---

## Conclusion
This project serves as a proof-of-concept AI prototype to explore AI-assisted resume screening.  
The focus is on understanding system flow and AI-driven analysis rather than production-level engineering.
