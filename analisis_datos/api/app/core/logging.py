"""Configuración del sistema de registro de eventos (logging)."""

import logging

from app.core.config import get_settings


def configure_logging() -> None:
    """
    Configura el sistema de registro de eventos de la aplicación.

    Establece el nivel de registro y el formato de los mensajes
    utilizando los valores definidos en la configuración de la
    aplicación.
    """

    settings = get_settings()

    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )