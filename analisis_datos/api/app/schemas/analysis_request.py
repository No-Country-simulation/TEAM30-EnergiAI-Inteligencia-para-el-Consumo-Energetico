"""
Modelos de entrada para el servicio de análisis energético.
"""

from pydantic import BaseModel, ConfigDict, Field


class AnalysisRequest(BaseModel):
    """
    Representa la información recibida desde el Backend para
    realizar el análisis energético de un hogar.
    """

    consumo_kwh: float = Field(
        ...,
        gt=0,
        description="Consumo energético registrado en kWh."
    )

    cantidad_personas: int = Field(
        ...,
        ge=1,
        description="Cantidad de personas que habitan el inmueble."
    )

    cantidad_equipos: int = Field(
        ...,
        ge=0,
        description="Cantidad de equipos eléctricos utilizados."
    )

    temperatura_exterior: float = Field(
        ...,
        description="Temperatura exterior registrada."
    )

    uso_horario_pico: bool = Field(
        ...,
        description="Indica si existe consumo durante horarios de alta demanda."
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "consumo_kwh": 420,
                "cantidad_personas": 4,
                "cantidad_equipos": 10,
                "temperatura_exterior": 28,
                "uso_horario_pico": True
            }
        }
    )