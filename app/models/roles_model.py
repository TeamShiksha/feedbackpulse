from typing import List
from sqlalchemy.orm import Mapped, Session, relationship
from app.models.base_model import Base, Short, Medium, Intpk
from app.models.enum_for_models import UserRole


class Role(Base):
    """
    Class representation of `roles` table present
    inside the database. Along with some helper functions.
    """

    __tablename__ = "roles"

    id: Mapped[Intpk]
    name: Mapped[Short]
    description: Mapped[Medium]

    users: Mapped[List["User"]] = relationship("User", back_populates="role") # type: ignore

    def __repr__(self) -> str:
        """
        Representation of the model data.
        """
        return f"Role(id={self.id!r}, name={self.name!r}, fullname={self.description!r})"

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