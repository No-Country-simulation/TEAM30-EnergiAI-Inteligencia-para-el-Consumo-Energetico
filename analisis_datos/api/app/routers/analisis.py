"""
Endpoints relacionados con el análisis energético.
"""

import logging

from fastapi import APIRouter

from app.schemas.analysis_request import AnalysisRequest
from app.schemas.analysis_response import AnalysisResponse
from app.services.business_service import BusinessService
from app.services.prediction_service import PredictionService

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="",
    tags=["Análisis Energético"],
)

prediction_service = PredictionService()
business_service = BusinessService()


@router.post(
    "/analisis-energetico",
    response_model=AnalysisResponse,
    summary="Realiza un análisis energético del hogar",
)
def analyze_energy(
    request: AnalysisRequest,
) -> AnalysisResponse:
    """
    Ejecuta el análisis energético utilizando el modelo de
    Machine Learning y las reglas de negocio.
    """

    logger.info("Iniciando análisis energético.")

    prediction = prediction_service.predict(request)

    response = business_service.process(
        request=request,
        prediction=prediction,
    )

    logger.info("Análisis energético finalizado.")

    return response