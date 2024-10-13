"""
Start of the application
"""

from flask import Flask
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_moment import Moment
from app.routes import auth_bp, public_bp
from app.models import Base, Role, Status, Project
from app.utils import load_enums
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

    app.register_blueprint(auth_bp, url_prefix= "/auth")
    app.register_blueprint(public_bp)
    print(app.url_map)

    app.cli.add_command(load_enums)

    return app
