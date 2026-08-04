"""
Servicio encargado de obtener la predicción energética.

Actualmente utiliza un predictor simulado mientras el modelo
de Machine Learning no se encuentre disponible.

Cuando CD3 entregue el archivo modelo.pkl únicamente será
necesario reemplazar la lógica interna de este servicio,
manteniendo intacto el resto del microservicio.
"""

import logging

from app.schemas.analysis_request import AnalysisRequest
from app.schemas.prediction_result import PredictionResult

logger = logging.getLogger(__name__)


class PredictionService:
    """
    Servicio responsable de obtener la predicción del modelo.
    """

    def predict(
        self,
        request: AnalysisRequest,
    ) -> PredictionResult:
        """
        Ejecuta una predicción simulada.

        Parameters
        ----------
        request : AnalysisRequest
            Información recibida para realizar el análisis.

        Returns
        -------
        PredictionResult
            Resultado simulado de la predicción.
        """

        logger.info(
            "Ejecutando predictor simulado para %.2f kWh.",
            request.consumo_kwh,
        )

        return PredictionResult(
            categoria="Moderado",
            probabilidad=0.86,
        )