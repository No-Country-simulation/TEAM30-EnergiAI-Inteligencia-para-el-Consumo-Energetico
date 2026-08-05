"""
Modelos de respuesta del servicio de análisis energético.
"""

from pydantic import BaseModel, ConfigDict, Field


class AnalysisResponse(BaseModel):
    """
    Representa la respuesta final del análisis energético.

    Contiene la predicción generada por el modelo de Machine Learning
    junto con las métricas y recomendaciones calculadas mediante
    las reglas de negocio.
    """

    categoria: str = Field(
        ...,
        description="Categoría de eficiencia energética predicha por el modelo."
    )

    probabilidad: float = Field(
        ...,
        ge=0,
        le=1,
        description="Nivel de confianza asociado a la predicción."
    )

    costo_estimado_mensual: float = Field(
        ...,
        description="Costo mensual estimado del consumo energético en USD."
    )

    ahorro_potencial_mensual: float = Field(
        ...,
        description="Ahorro potencial mensual estimado en USD."
    )

    ahorro_potencial_anual: float = Field(
        ...,
        description="Ahorro potencial anual estimado en USD."
    )

    recomendaciones: list[str] = Field(
        ...,
        description="Recomendaciones generadas por las reglas de negocio."
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "categoria": "Moderado",
                "probabilidad": 0.99,
                "costo_estimado_mensual": 315.00,
                "ahorro_potencial_mensual": 31.50,
                "ahorro_potencial_anual": 378.00,
                "recomendaciones": [
                    "El consumo energético mensual es elevado. Se recomienda identificar y optimizar los equipos de mayor demanda.",
                    "Evite concentrar el uso de equipos eléctricos durante los horarios de mayor demanda energética.",
                    "Existen oportunidades de mejora que pueden incrementar la eficiencia energética del hogar."
                ]
            }
        }
    )