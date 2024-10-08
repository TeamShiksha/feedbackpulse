import json
from sqlalchemy.orm import Mapped, Session
from .base_model import Base, Short, Medium, Intpk
from .enum_for_models import UserRole


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[Intpk]
    name: Mapped[Short]
    description: Mapped[Medium]

    def __repr__(self) -> str:
        """
        Json representation of the model data.
        """
        role = {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
        return json.dumps(role, indent=3)

    @staticmethod
    def insert_roles(session: Session) -> None:
        """
        Insert roles and descriptions into the 
        table if they do not exist.
        """
        for role in UserRole:
            existing_role = session.query(Role).filter_by(name=role.name).first()
            if not existing_role:
                new_role = Role(name=role.name, description=role.value)
                session.add(new_role)
            elif existing_role.description != role.value:
                existing_role.description = role.value
        session.commit()