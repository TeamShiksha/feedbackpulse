import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Common configuration for all the enviornment
    """

    PORT = 5000
    SECRET_KEY = os.environ.get("SECRET_KEY") or "very secret key"
    FLASK_APP = os.environ.get("FLASK_APP") or "app.py"
    SQLALCHEMY_TRACK_MODIFICATIONs = False
    GITHUB_CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.environ.get("GITHUB_CLIENT_SECRET")
    OAUTHLIB_INSECURE_TRANSPORT = False

    @staticmethod
    def init__app(app):
        """
        For taking the application instance
        """


class DevelopmentConfig(Config):
    """
    Development environment specific configurations
    """

    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = True
    OAUTHLIB_INSECURE_TRANSPORT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    """
    Development environment specific configurations
    """

    TESTING = True
    SQLALCHEMY_ECHO = True
    OAUTHLIB_INSECURE_TRANSPORT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, 'test-dev.sqlite')


class ProductionConfig(Config):
    """
    Development environment specific configurations
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "Production": ProductionConfig,
    "default": DevelopmentConfig
}
