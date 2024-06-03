from fastapi import APIRouter
from app.api.api_v1.endpoints import project, persona

api_router = APIRouter()
api_router.include_router(project.router, prefix="/projects", tags=["projects"])
api_router.include_router(persona.router, prefix="/personas", tags=["personas"])
