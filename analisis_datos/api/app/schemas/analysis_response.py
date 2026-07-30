"""
Modelos de respuesta del servicio de análisis energético.
"""

from pydantic import BaseModel, ConfigDict, Field


class AnalysisResponse(BaseModel):
    """
    Representa la respuesta final entregada al Backend
    después de ejecutar el modelo de Machine Learning
    y aplicar las reglas de negocio.
    """

    categoria: str = Field(
        ...,
        description="Clasificación energética obtenida por el modelo."
    )

    iee: int = Field(
        ...,
        description="Índice de Eficiencia Energética."
    )

    probabilidad: float = Field(
        ...,
        ge=0,
        le=1,
        description="Nivel de confianza de la predicción."
    )

    costo_estimado_mensual: float = Field(
        ...,
        description="Costo mensual estimado del consumo energético."
    )

    ahorro_potencial_mensual: float = Field(
        ...,
        description="Ahorro potencial mensual."
    )

    ahorro_potencial_anual: float = Field(
        ...,
        description="Ahorro potencial anual."
    )

    recomendaciones: list[str] = Field(
        ...,
        description="Lista de recomendaciones generadas por las reglas de negocio."
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "categoria": "Moderado",
                "iee": 67,
                "probabilidad": 0.86,
                "costo_estimado_mensual": 315.0,
                "ahorro_potencial_mensual": 31.5,
                "ahorro_potencial_anual": 378.0,
                "recomendaciones": [
                    "Reducir el uso de equipos durante los horarios pico.",
                    "Revisar los equipos con mayor consumo energético.",
                    "Optimizar el uso de electrodomésticos."
                ]
            }
        }
    )