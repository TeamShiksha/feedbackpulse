from typing import List
from sqlalchemy.orm import Mapped, Session, relationship
from .base_model import Base, Short, Medium, Intpk
from .enum_for_models import RequestStatus

class Status(Base):
    """
    Class representation of `statuses` table present 
    inside the database. Along with some helper functions.
    """

    __tablename__ = "statuses"

    id: Mapped[Intpk]
    name: Mapped[Short]
    description: Mapped[Medium]

    snapshots: Mapped[List["Snapshot"]] = relationship("Snapshot",\
                                                       back_populates="status")
    requests: Mapped[List["Request"]] = relationship("Request",\
                                                     back_populates="status")

    def __repr__(self) -> str:
        """
        Representation of the model data.
        """
        return f"Status(id={self.id!r}, name={self.name!r}, fullname={self.description!r})"
    
    @staticmethod
    def insert_statuses(session: Session) -> None:
        """
        Insert statuses and description inside
        table if they do not exists.
        """
        from app import db
        for status in RequestStatus:
            existing_role = session.query(Status).filter_by(name=status.name).first()
            if not existing_role:
                new_role = Status(name=status.name, description=status.value)
                session.add(new_role)
            elif existing_role.description != status.value:
                existing_role.description = status.value
        session.commit()
