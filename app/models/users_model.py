from typing import Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base_model import Base, Short, UUIDpk, Medium, Boolean


class User(Base):
    """
    Class representation of `users` table present
    inside the database. Along with some helper functions.
    """

    __tablename__ = "users"

    id: Mapped[UUIDpk]
    username: Mapped[Short]
    name: Mapped[Optional[Medium]]
    email: Mapped[Short]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    project_id: Mapped[Optional[int]] = mapped_column(ForeignKey("projects.id"))
    avatar_url: Mapped[Medium]
    linkedin_url: Mapped[Optional[Medium]]
    github_url: Mapped[Medium]
    twitter_url: Mapped[Optional[Medium]]
    is_headshot: Mapped[Boolean]
    is_deleted: Mapped[Boolean]
    is_teamshiksha_member: Mapped[Boolean]
    discord_username: Mapped[Optional[Short]]
    is_fully_verified: Mapped[Boolean]

    role: Mapped["Role"] = relationship("Role", back_populates="users")
    project: Mapped["Project"] = relationship("Project", back_populates="users")
    snapshots: Mapped[List["Snapshot"]] = relationship("Snapshot",\
                                            foreign_keys="[Snapshot.user_id]",\
                                            back_populates="user")
    reviews: Mapped[List["Snapshot"]] = relationship("Snapshot",\
                                            foreign_keys="[Snapshot.lead_id]",\
                                            back_populates="lead")
    requests: Mapped[List["Request"]] = relationship("Request",\
                                            back_populates="user")
    

