"""
Contains declarative base class for Flask-SQLalchemy
and common Annotated types used model columns. 
"""

from uuid import uuid4
from datetime import datetime,timezone
from typing import Annotated
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


Intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
UUIDpk = Annotated[str, mapped_column(primary_key=True, default=lambda: str(uuid4()))]
Short = Annotated[str, mapped_column(String(30), unique=True)]
Medium = Annotated[str, mapped_column(String(100))]
Long = Annotated[str, mapped_column(String(200))]
Verylong = Annotated[str, mapped_column(String(400))]
Boolean = Annotated[bool, mapped_column(default=False)]
CTimestamp = Annotated[datetime, mapped_column(nullable=False,\
                default=datetime.now(timezone.utc))]
UTimestamp = Annotated[datetime, mapped_column(nullable=False,\
                default=datetime.now(timezone.utc),\
                onupdate=datetime.now(timezone.utc))]


class Base(DeclarativeBase):
    """
    Base model for all other models
    """

    created_timestamp: Mapped[CTimestamp]
    updated_timestamp: Mapped[UTimestamp]
