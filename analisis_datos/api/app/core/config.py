"""Configuración de la aplicación."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Define la configuración de la aplicación cargada desde variables de entorno."""

    # ------------------------------------------------------------------
    # Información general de la aplicación
    # ------------------------------------------------------------------
    app_name: str = "EnergiAI API"
    app_version: str = "1.0.0"

    # ------------------------------------------------------------------
    # Reglas de negocio
    # ------------------------------------------------------------------
    energy_price: float = 0.75

    efficient_savings: float = 0.05
    moderate_savings: float = 0.10
    inefficient_savings: float = 0.20

    # ------------------------------------------------------------------
    # Configuración del modelo de Machine Learning
    # ------------------------------------------------------------------
    model_source: str = "local"

    model_path: str = "../models/modelo_iee_gradient_boosting.pkl"

    # Se utilizará cuando el modelo sea descargado desde
    # Oracle Cloud Infrastructure (Object Storage).
    model_bucket_url: str | None = None

    # ------------------------------------------------------------------
    # Integración con Cohere
    # ------------------------------------------------------------------
    cohere_api_key: str

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Obtiene una instancia única de la configuración de la aplicación.

    La configuración se carga desde las variables de entorno y se almacena
    en caché para evitar crear múltiples instancias durante la ejecución
    del microservicio.

    Returns:
        Settings: Configuración de la aplicación.
    """
    return Settings()