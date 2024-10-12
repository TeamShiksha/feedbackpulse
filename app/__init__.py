"""
Start of the application
"""

import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_moment import Moment
from app.models import Base, Role, Status, Project
from config import config


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
marshmallow = Marshmallow()
moment = Moment()
config_name = os.environ.get("FLASK_CONFIG").lower() or "default"

def create_app():
    """
    Factory method for creating and configuring the
    whole flask application
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init__app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    moment.init_app(app)

    with app.app_context():
        db.create_all()
        Role.insert_roles(db.session)
        Status.insert_statuses(db.session)
        Project.insert_projects(db.session)

    return app
