from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import Base, UUIDpk, Short, Long, Boolean


class Request(Base):
    """
    Class representation of `requests` table present
    inside the database. Along with some helper functions.
    """

    __tablename__ = "requests"

    id: Mapped[UUIDpk]
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    resource: Mapped[Short]
    justification: Mapped[Long]
    number_of_days: Mapped[int]
    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.id"))
    is_approved: Mapped[Boolean]
    is_deleted: Mapped[Boolean]

    project: Mapped["Project"] = relationship("Project", back_populates="requests")
    user: Mapped["User"] = relationship("User", back_populates="requests")
    status: Mapped["Status"] = relationship("Status", back_populates="requests")

    def __repr__(self):
        """
        Representation of the model data.
        """
        return (
            f"<Request(id={self.id}, project_id={self.project_id}, "
            f"user_id={self.user_id}, resource='{self.resource}', "
            f"justification='{self.justification}', number_of_days={self.number_of_days}, "
            f"status_id={self.status_id}, is_approved={self.is_approved}, "
            f"is_deleted={self.is_deleted})>"
        )
