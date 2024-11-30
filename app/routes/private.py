from flask import Blueprint, render_template
from app.utils.decorators import login_required

private_bp = Blueprint("private", __name__)

@private_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html"), 200

@private_bp.route("/projects")
@login_required
def projects():
    return render_template("projects.html"), 200

@private_bp.route("/snapshots")
@login_required
def snapshots():
    return render_template("snapshots.html"), 200

@private_bp.route("/resources")
@login_required
def resources():
    return render_template("resources.html"), 200