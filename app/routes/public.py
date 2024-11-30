from flask import Blueprint, render_template, redirect, url_for
from flask_dance.contrib.github import github

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def home():
    if github.authorized:
        return redirect(url_for("private.dashboard"))
    return render_template("home.html"), 200