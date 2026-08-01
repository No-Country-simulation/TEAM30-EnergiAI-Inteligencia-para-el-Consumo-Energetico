"""
Manejadores globales de excepciones de la aplicación.
"""

import logging

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Registra los manejadores globales de excepciones de la aplicación.

    Parameters
    ----------
    app : FastAPI
        Instancia principal de FastAPI.
    """

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        """
        Maneja errores de validación de los datos de entrada.
        """

        logger.warning(
            "Error de validación en la solicitud: %s",
            exc.errors(),
        )

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "codigo": 422,
                "error": "Error de validación",
                "detalle": exc.errors(),
            },
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException,
    ) -> JSONResponse:
        """
        Maneja excepciones HTTP controladas.
        """

        logger.warning(
            "Excepción HTTP: %s",
            exc.detail,
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "codigo": exc.status_code,
                "error": "Solicitud inválida",
                "detalle": exc.detail,
            },
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        """
        Maneja errores inesperados de la aplicación.
        """

        logger.exception(
            "Error interno no controlado: %s",
            exc,
        )

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "codigo": 500,
                "error": "Error interno del servidor",
                "detalle": (
                    "Ha ocurrido un error inesperado. "
                    "Intente nuevamente más tarde."
                ),
            },
        )