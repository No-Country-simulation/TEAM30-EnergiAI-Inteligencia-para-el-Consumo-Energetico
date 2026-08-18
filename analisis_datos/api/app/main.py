"""
Punto de entrada de la aplicación FastAPI.
"""
from fastapi import FastAPI
from app.routers.analisis import router as analysis_router
from app.exceptions.handlers import register_exception_handlers
from app.core.logging import setup_logging


setup_logging()
app = FastAPI(
    title="EnergiAI API",
    version="1.0.0",
    description="Microservicio de Inteligencia Artificial para el análisis energético.",
)

register_exception_handlers(app)
app.include_router(analysis_router)