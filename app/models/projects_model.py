from typing import List
from sqlalchemy.orm import Mapped, Session, relationship
from app.models.base_model import Base, Short, Long, Intpk
from app.models.enum_for_models import Projects


class Project(Base):
    """
    Class representation of `projects` table present 
    inside the database. Along with some helper functions.
    """

    __tablename__ = "projects"

    id: Mapped[Intpk]
    name: Mapped[Short]
    description: Mapped[Long]

    requests: Mapped[List["Request"]] = relationship("Request", back_populates="project")
    users: Mapped[List["User"]] = relationship("User", back_populates="project")
    snapshots: Mapped[List["Snapshot"]] = relationship("Snapshot", back_populates="project")

    def __repr__(self) -> str:
        """
        Representation of the model data.
        """
        return f"Project(id={self.id!r}, name={self.name!r}, fullname={self.description!r})"
    
    @staticmethod
    def insert_projects(session: Session) -> None:
        """
        Insert project and description inside
        table if they do not exists.
        """
        for project in Projects:
            existing_role = session.query(Project).filter_by(name=project.name).first()
            if not existing_role:
                new_role = Project(name=project.name, description=project.value)
                session.add(new_role)
            elif existing_role.description != project.value:
                existing_role.description = project.value
        session.commit()
