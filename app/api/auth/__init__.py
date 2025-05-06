from fastapi import APIRouter


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[
        # Depends(),
    ],
)


@auth_router.get("/sign-in")
async def sign_in():
    pass


@auth_router.get("/sign-up")
async def sign_up():
    pass
