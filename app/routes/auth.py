import os
from flask import Blueprint, redirect, url_for, flash, current_app
from flask_dance.contrib.github import make_github_blueprint, github
from app.utils.decorators import login_required

auth_bp = Blueprint("auth", __name__)
github_bp = make_github_blueprint(scope= "user:email")
auth_bp.register_blueprint(github_bp)

@auth_bp.route("/signin")
def signin():
    if not github.authorized:
        return redirect(url_for("auth.github.login"))
    resp = github.get("/user/emails")
    if not resp.ok:
        return redirect(url_for("public.home"))
    emails = resp.json()
    primary_email = next((email['email'] for email in emails if email['primary']), None)
    print(primary_email)
    return redirect(url_for('private.dashboard'))

@auth_bp.route("/signout")
@login_required
def signout():
    github_bp.token = None
    return redirect(url_for('public.home'))
