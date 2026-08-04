"""
Servicio encargado de aplicar las reglas de negocio al resultado
del modelo de Machine Learning.
"""

import logging

from app.core.config import get_settings
from app.schemas.analysis_request import AnalysisRequest
from app.schemas.analysis_response import AnalysisResponse
from app.schemas.prediction_result import PredictionResult

logger = logging.getLogger(__name__)


class BusinessService:
    """
    Servicio responsable de enriquecer la predicción del modelo
    con reglas de negocio.
    """

    def __init__(self) -> None:
        """
        Inicializa la configuración utilizada por las reglas de negocio.
        """
        self.settings = get_settings()

    def process(
        self,
        request: AnalysisRequest,
        prediction: PredictionResult,
    ) -> AnalysisResponse:
        """
        Construye la respuesta final del análisis energético.
        """

        logger.info("Aplicando reglas de negocio.")

        monthly_cost = self._calculate_monthly_cost(request.consumo_kwh)

        monthly_savings = self._calculate_monthly_savings(
            monthly_cost,
            prediction.categoria,
        )

        yearly_savings = self._calculate_yearly_savings(monthly_savings)

        recommendations = self._build_recommendations(
            request,
            prediction,
        )

        return AnalysisResponse(
            categoria=prediction.categoria,
            probabilidad=prediction.probabilidad,
            costo_estimado_mensual=monthly_cost,
            ahorro_potencial_mensual=monthly_savings,
            ahorro_potencial_anual=yearly_savings,
            recomendaciones=recommendations,
        )

    def _calculate_monthly_cost(self, consumo_kwh: float) -> float:
        """
        Calcula el costo estimado mensual.
        """
        return round(
            consumo_kwh * self.settings.energy_price,
            2,
        )

    def _calculate_monthly_savings(
        self,
        monthly_cost: float,
        category: str,
    ) -> float:
        """
        Calcula el ahorro potencial mensual según la categoría.
        """

        percentage = self._get_savings_percentage(category)

        return round(
            monthly_cost * percentage,
            2,
        )

    def _get_savings_percentage(
        self,
        category: str,
    ) -> float:
        """
        Obtiene el porcentaje de ahorro según la categoría energética.
        """

        if category == "Eficiente":
            return self.settings.efficient_savings

        if category == "Moderado":
            return self.settings.moderate_savings

        if category == "Ineficiente":
            return self.settings.inefficient_savings

        return 0.0

    def _calculate_yearly_savings(
        self,
        monthly_savings: float,
    ) -> float:
        """
        Calcula el ahorro potencial anual.
        """
        return round(
            monthly_savings * 12,
            2,
        )

    def _build_recommendations(
        self,
        request: AnalysisRequest,
        prediction: PredictionResult,
    ) -> list[str]:
        """
        Genera recomendaciones según las reglas de negocio.
        """

        recommendations: list[str] = []

        if request.uso_horario_pico:
            recommendations.append(
                "Reducir el consumo durante los horarios de mayor demanda."
            )

        if prediction.categoria == "Ineficiente":
            recommendations.append(
                "Revisar los equipos eléctricos de mayor consumo."
            )

        if request.temperatura_exterior >= 30:
            recommendations.append(
                "Optimizar el uso de sistemas de climatización."
            )

        if not recommendations:
            recommendations.append(
                "Mantener los hábitos actuales de consumo energético."
            )

        return recommendations