from logging import getLogger
from advanced_alchemy.extensions.fastapi import AdvancedAlchemy
from fastapi import FastAPI

from app.config.plugins import SQLALCHEMY_CONFIG

logger = getLogger(__name__)

# ================================================= ALCHEMY

alchemy = AdvancedAlchemy(config=SQLALCHEMY_CONFIG)


def setup_alchemy_app(app: FastAPI):
    alchemy.init_app(app)
    app.state.alchemy = alchemy


# ================================================= LOGGING


def setup_logging(app: FastAPI):
    import logging.config
    from app.config.plugins import LOGGING_CONFIG

    logging.config.dictConfig(LOGGING_CONFIG)


# =================================================
