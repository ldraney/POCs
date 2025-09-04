from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.config import settings
from app.routes import api

app = FastAPI(title=settings.APP_NAME)

# Mount static files
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

# Setup templates
templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)

# Include API routes
app.include_router(api.router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "pages/index.html",
        {"request": request, "title": "Namespace Service"}
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy", "app": settings.APP_NAME}