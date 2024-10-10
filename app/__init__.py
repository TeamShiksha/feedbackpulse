import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import Base, Role, Status, Project

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    """
    Factory
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dev-database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()
        Role.insert_roles(db.session)
        Status.insert_statuses(db.session)
        Project.insert_projects(db.session)

    return app
