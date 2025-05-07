from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Annotated
from advanced_alchemy.base import UUIDAuditBase
from advanced_alchemy.mixins import SlugKey
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

if TYPE_CHECKING:
    from .user import UserModel
else:
    UserModel = None


class SupportedFileFormats(Enum):
    DICOM = ".dcm"
    JPG = ".jpg"
    PNG = ".png"
    PDF = ".pdf"


timestamp = Annotated[datetime, mapped_column(nullable=False, server_default=func.now())]


class FileModel(UUIDAuditBase, SlugKey):
    __tablename__ = "file"
    __table_args__ = {"comment": "Represent a file uploaded by a user to minio."}

    file_name: Mapped[str] = mapped_column(nullable=False)
    file_type: Mapped[SupportedFileFormats] = mapped_column(nullable=False)
    file_size: Mapped[int] = mapped_column(nullable=False)
    hash_sum: Mapped[str] = mapped_column(nullable=False)
    upload_date: Mapped[timestamp] = mapped_column(nullable=False)
    path: Mapped[str] = mapped_column(nullable=False)

    description: Mapped[str | None]

    # =============================== Relationships

    # user: Mapped[list[User]] = relationship(
    #     back_populates="user",
    #     cascade="save-update, merge, delete",
    #     lazy="noload",
    #     viewonly=True,
    # )
