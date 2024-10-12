from flask import Blueprint, render_template

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def home():
    return render_template("home.html"), 200