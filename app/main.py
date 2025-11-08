"""
Create a FastAPI application that integrates with OpenAI's API to process resumes.
This application will read resumes from a specified directory, extract text from PDF files,
and use OpenAI's API to analyze the content of the resumes.

The application will also handle file uploads and provide endpoints for resume processing.

- Create an API endpoint to upload resumes.
- Create a function that reads the pdf files using the PyPDF2 library and extracts text.
- Use OpenAI's API to analyze the extracted text.
"""

from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from app.parsepdf import parse_pdf
from app.agents.resume_extractor_agent import analyze_resume
from app.agents.jd_extractor_agent import analyze_jd
from app.agents.candidate_evaluation_agent import evaluate_candidate
import json
from pathlib import Path

app = FastAPI()

@app.post("/screening/")
async def upload_resume(resume: UploadFile):
    """
    Endpoint to upload a resume file.
    """
    print("Received resume file:", resume.filename)

    resume_text = parse_pdf(resume.file)

    try:
        candidate_details = analyze_resume(resume_text)
        if isinstance(candidate_details, dict) and "error" in candidate_details:
            return JSONResponse(content={"error": "Failed to analyze resume: " + candidate_details["error"]}, status_code=500)

        jd_text = ""
        jd_path = Path(__file__).parent.parent / "resources" / "job_description.pdf"
        with open(jd_path, "rb") as file:
            jd_text = parse_pdf(file)

        jd_details = analyze_jd(jd_text)
        if isinstance(jd_details, dict) and "error" in jd_details:
            return JSONResponse(content={"error": "Failed to analyze job description: " + jd_details["error"]}, status_code=500)

        evaluation = evaluate_candidate(candidate_details, jd_details)
        if isinstance(evaluation, dict) and "error" in evaluation:
            return JSONResponse(content={"error": "Failed to evaluate candidate: " + evaluation["error"]}, status_code=500)

        print("Evaluation result:", evaluation)

        if isinstance(evaluation, str):
            try:
                result_json = json.loads(evaluation)
            except json.JSONDecodeError as e:
                return JSONResponse(content={"error": f"Failed to parse evaluation response: {str(e)}"}, status_code=500)
        else:
            result_json = evaluation  # In case it's already a dict, but shouldn't happen
        return JSONResponse(content=result_json)
    except Exception as e:
        print("Unexpected error:", str(e))
        return JSONResponse(content={"error": "Internal server error: " + str(e)}, status_code=500)
    
    