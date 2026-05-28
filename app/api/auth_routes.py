from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.auth.auth import register_user, verify_user

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/login")
async def login_page(request: Request):
    if request.session.get("user"):
        return RedirectResponse(url="/welcome", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def do_login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    success, display_name = verify_user(username, password)
    if success:
        request.session["user"] = username.strip().lower()
        request.session["display_name"] = display_name
        return RedirectResponse(url="/welcome", status_code=302)
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Invalid username or password. Please try again.",
        "active_tab": "login"
    })


@router.post("/register")
async def do_register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...)
):
    if password != confirm_password:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Passwords do not match.",
            "active_tab": "register"
        })
    success, message = register_user(username, password)
    if success:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "success": message,
            "active_tab": "login"
        })
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": message,
        "active_tab": "register"
    })


@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=302)
