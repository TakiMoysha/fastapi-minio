from typing import Annotated, AsyncGenerator

from advanced_alchemy.extensions.fastapi import AdvancedAlchemy
from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession


from app.server.plugins import alchemy
from app.domain.accounts.services import AccountService

__all__ = (
    "DepsAlchemy",
    "DepsAlchemySession",
    "DepsAccountsService",
)


async def provide_minio() -> AsyncGenerator:
    return None


# =====================================================================================================
def provide_alchemy(request: Request) -> AdvancedAlchemy:
    if request.app.state.alchemy is None:
        raise RuntimeError("Alchemy is not initialized")

    return request.app.state.alchemy


DepsAlchemy = Annotated[AdvancedAlchemy, Depends(provide_alchemy)]


def provide_async_session(alchemy: DepsAlchemy, request: Request) -> AsyncSession:
    return alchemy.get_async_session(request)


DepsAlchemySession = Annotated[AsyncSession, Depends(provide_async_session)]

# =====================================================================================================

# from typing import AsyncGenerator

# from app.domain.accounts.services import AccountService


# async def provide_accounts_service(db_session: DepsAlchemySession) -> AsyncGenerator[AccountService, None]:
#     async with AccountService.new(session=db_session) as service:
#         yield service


DepsAccountsService = Annotated[AccountService, Depends(alchemy.provide_service(AccountService))]

# DatabaseSession = Annotated[AsyncSession, Depends(get_alchemy().get_async_session())]
