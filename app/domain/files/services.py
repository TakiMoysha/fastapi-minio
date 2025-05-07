from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from fastapi import status

from app.config.consts import SUPERUSER_ROLE_NAME
from app.database.models.file import FileModel
from app.exceptions import PermissionDeniedException, WorkInProgressException

EXC_ERROR = "ERROR"


__all__ = ("FilesService",)


class FilesService(SQLAlchemyAsyncRepositoryService[FileModel]):
    class _FilesRepository(SQLAlchemyAsyncRepositoryService[FileModel]):
        model_type = FileModel  # type: ignore

    repository_type = _FilesRepository

    async def get_many_first(self, limit: int = 10) -> list[FileModel]:
        return await self.repository.list_and_count(limit=limit)
