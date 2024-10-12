import os
from flask import Blueprint, redirect, url_for, flash, current_app
from flask_dance.contrib.github import make_github_blueprint, github

auth_bp = Blueprint("auth", __name__)
github_bp = make_github_blueprint(scope= "user:email")
auth_bp.register_blueprint(github_bp)

@auth_bp.route("/signin")
def signin():
    if not github.authorized:
        return redirect(url_for("auth.github.login"))
    resp = github.get("/user/emails")
    if resp.ok:
        emails = resp.json()
        primary_email = next((email['email'] for email in emails if email['primary']), None)
        print(primary_email)
        flash('Signed in successfully!', 'success')
    else:
        flash('Failed to fetch email.', 'error')
    return redirect(url_for('home'))

@auth_bp.route("/signout")
def signout():
    github_bp.token = None
    flash('Signed out successfully!', 'info')
    return redirect(url_for('home'))
