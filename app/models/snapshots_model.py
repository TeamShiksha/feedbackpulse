from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import Base, Verylong, UUIDpk, Boolean


class Snapshot(Base):
    """
    Class representation of `snapshots` table present 
    inside the database. Along with some helper functions.
    """

    __tablename__ = "snapshots"

    id: Mapped[UUIDpk]
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    lead_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    description: Mapped[Verylong]
    comment: Mapped[Optional[Verylong]]
    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.id"))
    is_deleted: Mapped[Boolean]

    project: Mapped["Project"] = relationship("Project", back_populates="snapshots")
    user: Mapped["User"] = relationship("User", foreign_keys=[user_id],\
                                        back_populates="snapshots")
    lead: Mapped["User"] = relationship("User", foreign_keys=[lead_id],\
                                        back_populates="reviews")
    status: Mapped["Status"] = relationship("Status", back_populates="snapshots")

    def __repr__(self):
        """
        Representation of the model data.
        """
        return (
            f"<Snapshot(id={self.id}, user_id={self.user_id}, lead_id={self.lead_id}, "
            f"project_id={self.project_id}, description='{self.description}', "
            f"comment='{self.comment}', status_id={self.status_id}, "
            f"is_deleted={self.is_deleted})>"
        )
