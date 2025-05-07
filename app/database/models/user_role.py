from datetime import UTC, datetime
from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TC003

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .role import RoleModel
    from .user import UserModel
else:
    RoleModel = None
    UserModel = None


class UserRoleModel(UUIDAuditBase):
    __tablename__ = "user_account_role"
    __table_args__ = {"comment": "Links a user to a specific role."}

    user_id: Mapped[UUID] = mapped_column(ForeignKey("user_account.id", ondelete="cascade"), nullable=False)
    role_id: Mapped[UUID] = mapped_column(ForeignKey("role.id", ondelete="cascade"), nullable=False)
    assigned_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))

    # =============================== Relationships

    user: Mapped[UserModel] = relationship(back_populates="roles", innerjoin=True, uselist=False, lazy="joined")
    user_name: AssociationProxy[str] = association_proxy("user", "name")
    user_email: AssociationProxy[str] = association_proxy("user", "email")

    role: Mapped[RoleModel] = relationship(back_populates="users", innerjoin=True, uselist=False, lazy="joined")
    role_name: AssociationProxy[str] = association_proxy("role", "name")
    role_slug: AssociationProxy[str] = association_proxy("role", "slug")
