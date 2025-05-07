from logging import getLogger

from app.server.lifespan import app_lifespan


logger = getLogger(__name__)


def create_asgi():
    from fastapi import FastAPI
    from fastapi.middleware import Middleware
    from fastapi.middleware.cors import CORSMiddleware

    from app.__about__ import __version__
    from app.config import get_config
    from app.api.router import api_router as api_router
    from app.server.plugins import setup_logging, setup_alchemy_app

    config = get_config()

    app = FastAPI(
        title="FastAPI-MinIO",
        version=__version__,
        debug=config.server.debug,
        lifespan=app_lifespan,
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_credentials=True,
                allow_origins=config.server.cors_origins,
                allow_methods=config.server.cors_methods,
                allow_headers=config.server.cors_headers,
            ),
        ],
    )

    setup_alchemy_app(app)
    setup_logging(app)

    app.include_router(api_router)

    return app
