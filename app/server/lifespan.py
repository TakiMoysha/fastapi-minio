from contextlib import asynccontextmanager
from logging import getLogger

from fastapi import FastAPI

from .plugins import alchemy

logger = getLogger(__name__)


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    """"""
    app.state.alchemy = alchemy
    logger.info(f"app_lifespan: <{str(app.state.alchemy)}>")
    yield
