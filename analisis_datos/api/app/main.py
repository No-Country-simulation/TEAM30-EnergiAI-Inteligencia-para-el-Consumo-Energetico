"""
Punto de entrada de la aplicación FastAPI.
"""

from fastapi import FastAPI

from app.routers.analisis import router as analysis_router

app = FastAPI(
    title="EnergiAI API",
    version="1.0.0",
    description="Microservicio de Inteligencia Artificial para el análisis energético.",
)

app.include_router(analysis_router)