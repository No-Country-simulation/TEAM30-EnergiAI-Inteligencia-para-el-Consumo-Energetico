"""Configuración de la aplicación."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Define la configuración de la aplicación cargada desde variables de entorno."""

    app_name: str = "EnergiAI API"
    app_version: str = "1.0.0"

    energy_price: float = 0.55
    
    efficient_savings: float = 0.05

    moderate_savings: float = 0.10

    inefficient_savings: float = 0.20

    model_path: str = "../models/modelo.pkl"

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Obtiene una instancia de la configuración de la aplicación.

    La instancia se almacena en caché mediante ``lru_cache`` para
    evitar crear múltiples objetos de configuración durante la
    ejecución de la aplicación.

    Returns:
        Settings: Instancia única con la configuración de la aplicación.
    """
    return Settings()