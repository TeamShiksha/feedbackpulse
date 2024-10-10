"""
Contains declarative base class for Flask-SQLalchemy
and common Annotated types used model columns. 
"""

from uuid import uuid4
from datetime import datetime
from typing import Annotated
from sqlalchemy import String, func
from sqlalchemy.orm import DeclarativeBase, mapped_column


Intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
UUIDpk = Annotated[str, mapped_column(primary_key=True, default=uuid4)]
Short = Annotated[str, mapped_column(String(30))]
Medium = Annotated[str, mapped_column(String(100))]
Long = Annotated[str, mapped_column(String(200))]
Verylong = Annotated[str, mapped_column(String(400))]
Boolean = Annotated[bool, mapped_column(default=False)]
CTimestamp = Annotated[datetime, mapped_column(nullable=False,\
                default=func.CURRENT_TIMESTAMP())]
UTimestamp = Annotated[datetime, mapped_column(nullable=False,\
                default=func.CURRENT_TIMESTAMP(),\
                onupdate=func.CURRENT_TIMESTAMP())]


class Base(DeclarativeBase):
    """
    Base model for all other models
    """
    pass
