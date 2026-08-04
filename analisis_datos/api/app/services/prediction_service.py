"""
Servicio encargado de cargar el modelo de Machine Learning y
realizar predicciones sobre el consumo energético.
"""

from pathlib import Path
import logging

import joblib
import pandas as pd

from app.core.config import get_settings
from app.schemas.analysis_request import AnalysisRequest
from app.schemas.prediction_result import PredictionResult

logger = logging.getLogger(__name__)

settings = get_settings()


class PredictionService:
    """
    Servicio responsable de cargar el modelo y ejecutar predicciones.
    """

    def __init__(self) -> None:
        """
        Inicializa el servicio cargando el modelo en memoria.
        """
        self._model = self._load_model()

    def _load_model(self):
        """
        Carga el modelo entrenado desde el sistema de archivos.

        Returns
        -------
        GradientBoostingClassifier
            Modelo cargado en memoria.

        Raises
        ------
        FileNotFoundError
            Si el archivo del modelo no existe.
        """
        model_path = Path(settings.model_path)

        logger.info("Cargando modelo desde: %s", model_path)

        if not model_path.exists():
            logger.error("No se encontró el modelo en %s", model_path)
            raise FileNotFoundError(
                f"No se encontró el modelo: {model_path}"
            )

        model = joblib.load(model_path)

        logger.info("Modelo cargado correctamente.")

        return model

    @staticmethod
    def _prepare_features(
        request: AnalysisRequest,
    ) -> pd.DataFrame:
        """
        Convierte la solicitud en un DataFrame compatible con el modelo.

        Parameters
        ----------
        request : AnalysisRequest
            Datos recibidos desde la API.

        Returns
        -------
        pandas.DataFrame
            Datos preparados para la predicción.
        """

        return pd.DataFrame(
            [
                {
                    "consumo_kwh": request.consumo_kwh,
                    "cantidad_personas": request.cantidad_personas,
                    "cantidad_equipos": request.cantidad_equipos,
                    "temperatura_exterior": request.temperatura_exterior,
                    "uso_horario_pico": int(request.uso_horario_pico),
                }
            ]
        )

    def predict(
        self,
        request: AnalysisRequest,
    ) -> PredictionResult:
        """
        Ejecuta una predicción utilizando el modelo entrenado.

        Parameters
        ----------
        request : AnalysisRequest
            Datos enviados por el Backend.

        Returns
        -------
        PredictionResult
            Categoría predicha y probabilidad asociada.
        """

        logger.info(
            "Iniciando predicción para %.2f kWh.",
            request.consumo_kwh,
        )

        features = self._prepare_features(request)

        prediction = self._model.predict(features)[0]

        probabilities = self._model.predict_proba(features)[0]

        class_index = list(self._model.classes_).index(prediction)

        probability = float(probabilities[class_index])

        logger.info(
            "Predicción completada. Categoría=%s Probabilidad=%.4f",
            prediction,
            probability,
        )

        return PredictionResult(
            categoria=prediction,
            probabilidad=round(probability, 2),
        )