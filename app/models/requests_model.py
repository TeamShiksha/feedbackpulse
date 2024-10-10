from sqlalchemy.orm import Mapped
from .base_model import (Base, UUIDpk, Long, CTimestamp,
                        UTimestamp, Boolean)

class Request(Base):
    """
    Class representation of `requests` table present
    inside the database. Along with some helper functions.
    """

    __tablename__ = "requests"

    id: Mapped[UUIDpk]
    project_id: Mapped[int]
    user_id: Mapped[str]
    resource: Mapped[str]
    justification: Mapped[Long]
    number_of_days: Mapped[int]
    status_id: Mapped[int]
    is_approved: Mapped[Boolean]
    is_deleted: Mapped[Boolean]
    created_timestamp: Mapped[CTimestamp]
    updated_timestamp: Mapped[UTimestamp]