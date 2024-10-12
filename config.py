import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Common configuration for all the enviornment
    """

    FLASK_DEBUG = False
    FLASK_RUN_PORT = os.environ.get("PORT") or 5000
    SECRET_KEY = os.environ.get("SECRET_KEY") or "very secret key"
    SQLALCHEMY_TRACK_MODIFICATIONs = False
    GITHUB_OAUTH_CLIENT_ID = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
    GITHUB_OAUTH_CLIENT_SECRET = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")

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
    Testing environment specific configurations
    """

    TESTING = True
    SQLALCHEMY_ECHO = True
    OAUTHLIB_INSECURE_TRANSPORT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    """
    Production environment specific configurations
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "Production": ProductionConfig,
    "default": DevelopmentConfig
}
