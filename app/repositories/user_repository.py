from app.models import User

from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    """
    UserRepository for user specific functionality
    """

    def __init__(self) -> None:
        super().__init__(User)
