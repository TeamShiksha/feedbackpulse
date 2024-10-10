import json
from sqlalchemy.orm import Mapped, Session
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

    def __repr__(self) -> str:
        """
        Json representation of the model data.
        """
        project = {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
        return json.dumps(project, indent=3)
    
    @staticmethod
    def insert_statuses(session: Session) -> None:
        """
        Insert statuses and description inside
        table if they do not exists.
        """
        for status in RequestStatus:
            existing_role = session.query(Status).filter_by(name=status.name).first()
            if not existing_role:
                new_role = Status(name=status.name, description=status.value)
                session.add(new_role)
            elif existing_role.description != status.value:
                existing_role.description = status.value
        session.commit()
