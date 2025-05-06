from fastapi import APIRouter


users_router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[
        # Depends(),
    ],
)


@users_router.get("/me")
async def read_users_me():
    return {"user_id": "the current user"}
