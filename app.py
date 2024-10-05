"""
feedbackpulse: Web app starts here.
"""

import os
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
github_bp = make_github_blueprint(
    client_id = os.getenv("GITHUB_CLIENT_ID"),
    client_secret = os.getenv("GITHUB_CLIENT_SECRET"),
    scope="user:email"
)

app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.register_blueprint(github_bp, url_prefix="/login")

@app.route("/")
def home():
    """
    Landing page of the app with GitHub OAuth login. This is to
    make sure only teamshiksha github org members can use this
    web application.
    """
    resp = github.get("/user")
    resp_emails = github.get("/user/emails")
    print(resp.json())
    print(resp_emails.json())
    # if current_user.is_authenticated:
    #     return redirect(url_for('dashboard'))
    return render_template("home.html"), 200
@app.route("/signout")
def signout():
    github_bp.token = None
    return redirect(url_for("home"))

@app.route("/signin")
def signin():
    """
    Landing page of the app with GitHub OAuth login. This is to
    make sure only teamshiksha github org members can use this
    web application.
    """
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    if resp.ok:
        github_info = resp.json()
        print(github_info)
        return redirect(url_for("dashboard"))
    return render_template("dashboard.html"), 200

@app.route("/dashboard")
# @login_required
def dashboard():
    """
    Landing page of the app with GitHub OAuth login. This is to
    make sure only teamshiksha github org members can use this
    web application.
    """
    return render_template("dashboard.html"), 200


if __name__ == "__main__":
    app.run()
