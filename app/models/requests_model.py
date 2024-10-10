from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import Base, UUIDpk, Long, Boolean


class Request(Base):
    """
    Class representation of `requests` table present
    inside the database. Along with some helper functions.
    """

    __tablename__ = "requests"

    id: Mapped[UUIDpk]
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    resource: Mapped[str]
    justification: Mapped[Long]
    number_of_days: Mapped[int]
    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.id"))
    is_approved: Mapped[Boolean]
    is_deleted: Mapped[Boolean]

    project: Mapped["Project"] = relationship("Project", back_populates="requests")
    user: Mapped["User"] = relationship("User", back_populates="requests")
    status: Mapped["Status"] = relationship("Status", back_populates="requests")