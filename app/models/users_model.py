from typing import Optional
from sqlalchemy.orm import Mapped
from app.models.base_model import (Base, Short, UUIDpk, Medium,
                        CTimestamp, UTimestamp, Boolean)

class User(Base):
    """
    Class representation of `users` table present
    inside the database. Along with some helper functions.
    """

    __tablename__ = "users"

    id: Mapped[UUIDpk]
    username: Mapped[Short]
    name: Mapped[Optional[Short]]
    email: Mapped[Short]
    role_id: Mapped[int]
    project_id: Mapped[Optional[int]]
    avatar_url: Mapped[Medium]
    linkedin_url: Mapped[Optional[Medium]]
    github_url: Mapped[Medium]
    twitter_url: Mapped[Optional[Medium]]
    is_headshot: Mapped[Boolean]
    is_deleted: Mapped[Boolean]
    is_teamshiksha_member: Mapped[Boolean]
    discord_username: Mapped[Optional[Short]]
    is_fully_verified: Mapped[Boolean]
    created_timestamp: Mapped[CTimestamp]
    updated_timestamp: Mapped[UTimestamp]

