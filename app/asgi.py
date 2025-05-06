def create_asgi():
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware

    from app.__about__ import __version__
    from app.config import get_config, consts
    from app.server.plugins import LoggingPlugin

    LoggingPlugin().setup_logging()

    config = get_config()

    app = FastAPI(
        title="FastAPI-MinIO",
        version=__version__,
        dependencies=[],
        debug=config.server.debug,
        docs_url=consts.OPENAPI_SCHEMA,
        routes=[],
        on_startup=[],
        lifespan=None,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=config.server.cors_origins,
        allow_methods=config.server.cors_methods,
        allow_headers=config.server.cors_headers,
    )

    return app


application = create_asgi()
