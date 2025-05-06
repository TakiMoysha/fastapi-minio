from enum import Enum
from typing import TYPE_CHECKING
from advanced_alchemy.base import UUIDAuditBase
from advanced_alchemy.mixins import SlugKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User


class SupportedFileFormats(Enum):
    DICOM = ".dcm"
    JPG = ".jpg"
    PNG = ".png"
    PDF = ".pdf"


class AttachmentFile(UUIDAuditBase, SlugKey):
    __tablename__ = "file"
    __table_args__ = {"comment": "Represent a file uploaded by a user to minio."}

    file_name: Mapped[str] = mapped_column(unique=False, nullable=False)
    file_type: Mapped[SupportedFileFormats] = mapped_column(unique=False, nullable=False)
    file_size: Mapped[int] = mapped_column(unique=False, nullable=False)
    upload_date: Mapped[str] = mapped_column(unique=False, nullable=False, server_default="now()")
    hash_sum: Mapped[str] = mapped_column(unique=False, nullable=False)
    minio_path: Mapped[str] = mapped_column(unique=False, nullable=False)

    description: Mapped[str | None]

    # =============================== Relationships

    user: Mapped[list[User]] = relationship(
        back_populates="user",
        cascade="save-update, merge, delete",
        lazy="noload",
        viewonly=True,
    )
