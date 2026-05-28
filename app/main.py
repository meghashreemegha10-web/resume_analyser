from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.middleware.sessions import SessionMiddleware
from app.core.config import settings
from app.api.endpoints import router as api_router
from app.api.auth_routes import router as auth_router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# Session middleware — required for login sessions
app.add_middleware(SessionMiddleware, secret_key="resume-analyzer-secret-key-2024")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Favicon & Chrome DevTools silence
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("app/static/favicon.png")

@app.get("/.well-known/appspecific/com.chrome.devtools.json", include_in_schema=False)
async def chrome_devtools_json():
    return {}

# Routers
app.include_router(auth_router)
app.include_router(api_router)
