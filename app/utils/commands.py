import click
from flask.cli import with_appcontext


@click.command("enum")
@with_appcontext
def load_enums():
    """
    Loads the enum tables in DB
    """
    from app.models import Role, Status, Project
    from app import db
    
    Role.insert_roles(db.session)
    Status.insert_statuses(db.session)
    Project.insert_projects(db.session)