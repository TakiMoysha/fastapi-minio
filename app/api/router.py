from logging import getLogger
from fastapi import APIRouter, Depends, HTTPException, status

from minio import Minio
from pydantic import EmailStr

from app.dependencies import (
    DepsAccountsService,
    DepsAlchemy,
    DepsAlchemySession,
    provide_minio,
    provide_retrieval_model,
)
from app.domain.accounts.services import AccountService
from app.lib.health_check import is_minio_healthy, is_model_loaded

logger = getLogger(__name__)

api_router = APIRouter(
    prefix="/api",
    tags=[],
    dependencies=[],
)


@api_router.get("/health", status_code=status.HTTP_200_OK, tags=["health"])
async def health_get(
    minio: Minio = Depends(provide_minio),
    retrieval_model=Depends(provide_retrieval_model),
):
    detail = {
        "minio": "ok" if is_minio_healthy(minio) else "error",
        "retrieval_model": "ok" if is_model_loaded(retrieval_model) else "error",
    }

    if all(value == "ok" for value in detail.values()):
        return {"status": "ok", "detail": detail}
    else:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=detail,
        )


# ================================================================================================
router = APIRouter(tags=["auth", "accounts"])

from pydantic.types import SecretStr

from app.lib.schemas import BaseSchema


class AccountRegistrionSchema(BaseSchema):
    email: EmailStr
    password: SecretStr


@router.post(
    "/auth/sign-up",
    status_code=status.HTTP_201_CREATED,
)
async def registration(
    input: AccountRegistrionSchema,
    accounts_service: DepsAccountsService,
):
    # res = await accounts_service.registration(email=input.email, password=input.password)
    res = await accounts_service.get_one_or_none(email=input.email)
    logger.info(f"registration: <{str(res)}>")
    return {"done": "OK"}


# @test_router.get(path="/accounts/me", response_model=UserModel)
# async def get_herself(
#     accounts_service: AccountsService,
#     user: CurrentUser,
# ):
#     return user


# @router.get(path="/accounts")
# async def list_users(
#     accounts_service: AccountsService,
# ):
#     logger.info(f"list_users: <{str(accounts_service)}>")
#     results, total = await accounts_service.get_many_first(limit=10)
#     logger.info(f"list_users: <{str(results), total}>")
#     return {
#         "results": results,
#         "total": total,
#     }


api_router.include_router(router)
