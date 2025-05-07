from fastapi import APIRouter

from fastapi import File, UploadFile


file_router = APIRouter(
    prefix="/files",
    tags=["files"],
    dependencies=[],
)


@file_router.post("/upload")
async def read_users_me(file: UploadFile):
    file_info = {
        "Filename": file.filename,
        "Format": file.content_type,
        "Size": file.size,
    }
    return {"file": file_info}
