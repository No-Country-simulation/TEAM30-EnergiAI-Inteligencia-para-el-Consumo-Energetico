"""
Configuración centralizada del sistema de logging.
"""

import logging


def setup_logging() -> None:
    """
    Configura el sistema de logging de la aplicación.
    """

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)-8s | "
            "%(name)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True,
    )