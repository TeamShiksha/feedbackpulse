# userservice class with static function
# a single service can call multiple repository functions
# does seperating the businss logic and data logic in different places
from app.repositories.user_repository import UserRepository

class UserService:

    user_repository = UserRepository()

    # @staticmethod
    # def some_random():
    #     return UserService.getsomething()