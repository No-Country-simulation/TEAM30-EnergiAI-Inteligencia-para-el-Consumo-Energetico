"""
Servicio encargado de cargar el modelo de Machine Learning y
realizar predicciones sobre el consumo energético.
"""

from pathlib import Path
import logging
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

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

    def _download_model(self, model_path: Path) -> None:
        """
        Descarga el modelo desde Oracle Cloud Infrastructure.

        Parameters
        ----------
        model_path : Path
            Ruta local donde se almacenará el modelo.

        Raises
        ------
        ValueError
            Si no se configuró la URL del modelo.
        RuntimeError
            Si ocurre un error durante la descarga.
        """
        if not settings.model_bucket_url:
            logger.error(
                "MODEL_BUCKET_URL no está configurado para MODEL_SOURCE=oci."
            )
            raise ValueError(
                "MODEL_BUCKET_URL es obligatorio cuando MODEL_SOURCE=oci."
            )

        logger.info(
            "Descargando modelo desde OCI: %s",
            settings.model_bucket_url,
        )

        try:
            # Crear el directorio si todavía no existe.
            model_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            with urlopen(settings.model_bucket_url) as response:
                model_path.write_bytes(response.read())

            logger.info(
                "Modelo descargado correctamente en: %s",
                model_path,
            )

        except (HTTPError, URLError, OSError) as exc:
            logger.exception(
                "Error al descargar el modelo desde OCI."
            )
            raise RuntimeError(
                "No se pudo descargar el modelo desde OCI."
            ) from exc

    def _load_model(self):
        """
        Carga el modelo entrenado desde el sistema de archivos
        o lo descarga desde OCI cuando MODEL_SOURCE=oci.

        Returns
        -------
        GradientBoostingClassifier
            Modelo cargado en memoria.

        Raises
        ------
        FileNotFoundError
            Si el modelo local no existe y no puede descargarse.
        ValueError
            Si la configuración de MODEL_SOURCE no es válida.
        """
        model_path = Path(settings.model_path)

        logger.info(
            "Origen del modelo configurado: %s",
            settings.model_source,
        )

        # --------------------------------------------------------------
        # Modelo desde OCI
        # --------------------------------------------------------------
        if settings.model_source.lower() == "oci":

            if not model_path.exists():
                logger.info(
                    "El modelo no existe localmente. "
                    "Se descargará desde OCI."
                )

                self._download_model(model_path)

            else:
                logger.info(
                    "Modelo encontrado localmente. "
                    "No es necesario descargarlo."
                )

        # --------------------------------------------------------------
        # Modelo local
        # --------------------------------------------------------------
        elif settings.model_source.lower() == "local":

            logger.info(
                "Utilizando modelo local."
            )

        # --------------------------------------------------------------
        # Origen no válido
        # --------------------------------------------------------------
        else:
            logger.error(
                "MODEL_SOURCE no válido: %s",
                settings.model_source,
            )

            raise ValueError(
                "MODEL_SOURCE debe ser 'local' o 'oci'."
            )

        # --------------------------------------------------------------
        # Verificar que el modelo exista antes de cargarlo
        # --------------------------------------------------------------
        if not model_path.exists():
            logger.error(
                "No se encontró el modelo en %s",
                model_path,
            )

            raise FileNotFoundError(
                f"No se encontró el modelo: {model_path}"
            )

        logger.info(
            "Cargando modelo desde: %s",
            model_path,
        )

        model = joblib.load(model_path)

        logger.info(
            "Modelo cargado correctamente."
        )

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