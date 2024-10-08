from flask import Flask
import os
from app.models import Base, Role, Status, Project
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(model_class=Base)
basedir = os.path.abspath(os.path.dirname(__file__))
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dev-database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)

    with app.app_context():
        db.create_all()
        Role.insert_roles(db.session)
        Status.insert_statuses(db.session)
        Project.insert_projects(db.session)

    return app

