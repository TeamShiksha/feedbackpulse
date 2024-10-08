import json
from sqlalchemy.orm import Mapped, Session
from .base_model import Base, Short, Long, Intpk
from .enum_for_models import Projects

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[Intpk]
    name: Mapped[Short]
    description: Mapped[Long]

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
