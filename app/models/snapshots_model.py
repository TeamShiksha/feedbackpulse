from typing import Optional
from sqlalchemy.orm import Mapped
from .base_model import (Base, Verylong, UUIDpk,
                        CTimestamp, UTimestamp, Boolean)


class Snapshot(Base):
    __tablename__ = "snapshots"

    id: Mapped[UUIDpk]
    user_id: Mapped[str]
    lead_id: Mapped[str]
    project_id: Mapped[int]
    description: Mapped[Verylong]
    comment: Mapped[Optional[Verylong]]
    status_id: Mapped[int]
    is_deleted: Mapped[Boolean]
    created_timestamp: Mapped[CTimestamp]
    updated_timestamp: Mapped[UTimestamp]