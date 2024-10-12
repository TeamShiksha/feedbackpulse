"""
Start of the application
"""

from flask import Flask
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_moment import Moment
from app.models import Base, Role, Status, Project
from config import config

load_dotenv()

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
marshmallow = Marshmallow()
moment = Moment()


def create_app(config_name: str = "default"):
    """
    Factory method for creating and configuring the
    whole flask application
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name.lower()])
    config[config_name].init__app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    moment.init_app(app)

    @app.cli.command()
    def enum():
        """
        Loads the enum tables in DB
        """
        Role.insert_roles(db.session)
        Status.insert_statuses(db.session)
        Project.insert_projects(db.session)

    return app
