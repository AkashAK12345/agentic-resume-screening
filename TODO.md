# TODO for Fixing ModuleNotFoundError in app/main.py

- [x] Update imports in app/main.py to relative imports (e.g., from .parsepdf import parse_pdf)
- [x] Update the file path for job_description.pdf to be relative using pathlib
- [x] Test the application to ensure the error is resolved
- [x] Verified FastAPI server starts without import errors on port 8005
- [x] Updated Streamlit UI to use port 8005
- [x] Started Streamlit UI on port 8505
- [x] Tested PDF parsing functionality: sample_resume.pdf and job_description.pdf parse correctly (minor warning for sample_resume.pdf)
- [ ] Note: Google Gemini API quota exceeded; full end-to-end testing requires API quota reset or upgrade
