from decouple import config  # pylint: disable=E0401
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.externals.ports.infrastructures.i_http_config_infrastructure import (
    IHttpServerConfigStructure,
)
from src.externals.routers.currency_exchange_router import CurrencyExchangeRouter


class FastApiHttpServerConfigInfrastructure(IHttpServerConfigStructure):
    def __init__(self):
        self.__app = FastAPI(
            title="Jaya",
            description="",
            docs_url="/docs",
            openapi_url="/openapi.json",
        )

    def __register_middlewares(self):
        cors_allowed_origins_str = config("CORS_ALLOWED_ORIGINS")
        cors_allowed_origins = cors_allowed_origins_str.split(",")
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __register_routers(self):
        currency_exchange_router = CurrencyExchangeRouter.get_router()

        self.__app.include_router(currency_exchange_router)

    def config_http_server(self) -> FastAPI:
        self.__register_middlewares()
        self.__register_routers()
        return self.__app
