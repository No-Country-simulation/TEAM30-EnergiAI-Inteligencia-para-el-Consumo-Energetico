"""
Modelo que representa la salida generada por el modelo de Machine Learning.

Este contrato corresponde exclusivamente al resultado entregado por CD3,
antes de aplicar las reglas de negocio de CD4.
"""

from pydantic import BaseModel, ConfigDict, Field


class PredictionResult(BaseModel):
    """
    Representa la predicción generada por el modelo de Machine Learning.
    """

    categoria: str = Field(
        ...,
        description="Clasificación energética obtenida por el modelo."
    )

    probabilidad: float = Field(
        ...,
        ge=0,
        le=1,
        description="Nivel de confianza de la predicción."
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "categoria": "Moderado",
                "probabilidad": 0.86
            }
        }
    )