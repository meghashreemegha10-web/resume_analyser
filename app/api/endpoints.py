from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.services.parser import ResumeParser
from app.services.analyzer import ResumeAnalyzer
import shutil
import os
import uuid
import tempfile

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

parser = ResumeParser()
analyzer = ResumeAnalyzer()


def get_user_context(request: Request) -> dict:
    """Return common template context with user info, or redirect if not logged in."""
    user = request.session.get("user")
    display_name = request.session.get("display_name", "User")
    return {"user": user, "display_name": display_name}


def require_auth(request: Request):
    """Returns redirect response if not authenticated, else None."""
    if not request.session.get("user"):
        return RedirectResponse(url="/login", status_code=302)
    return None


@router.get("/welcome")
async def welcome_page(request: Request):
    guard = require_auth(request)
    if guard:
        return guard
    ctx = get_user_context(request)
    return templates.TemplateResponse("welcome.html", {"request": request, **ctx})


@router.get("/")
async def get_upload_page(request: Request):
    guard = require_auth(request)
    if guard:
        return guard
    ctx = get_user_context(request)
    return templates.TemplateResponse("index.html", {"request": request, **ctx})


@router.post("/analyze")
async def analyze_resume(request: Request, file: UploadFile = File(...)):
    guard = require_auth(request)
    if guard:
        return guard

    ctx = get_user_context(request)

    # Validate file type
    if not file.filename.lower().endswith(('.pdf', '.docx', '.doc')):
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Invalid file type. Only PDF and DOCX are supported.",
            **ctx
        })

    # Save file temporarily
    filename = f"{uuid.uuid4()}_{file.filename}"
    upload_dir = os.path.join(tempfile.gettempdir(), "uploads")
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Parse
        parsed_data = await parser.parse_file(file_path, file.filename)

        # Analyze
        analysis_result = analyzer.analyze(parsed_data.text)

        return templates.TemplateResponse("result.html", {
            "request": request,
            "filename": file.filename,
            "score": analysis_result.score,
            "summary": analysis_result.summary,
            "found_skills": analysis_result.found_skills,
            "missing_skills": analysis_result.missing_critical_skills,
            "skills_score": analysis_result.skills_score,
            "structure_score": analysis_result.structure_score,
            "experience_score": analysis_result.experience_score,
            "readability_score": analysis_result.readability_score,
            "sections_found": analysis_result.sections_found,
            "sections_missing": analysis_result.sections_missing,
            "action_verb_count": analysis_result.action_verb_count,
            "estimated_years": analysis_result.estimated_years,
            "feedback_notes": analysis_result.feedback_notes,
            **ctx
        })

    except Exception as e:
        print(f"Error analyzing resume: {e}")
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": f"Error processing resume: {str(e)}",
            **ctx
        })
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
