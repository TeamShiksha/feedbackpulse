"""
feedbackpulse: Web app starts here.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """
    Landing page of the app with GitHub OAuth login. This is to
    make sure only teamshiksha github org members can use this
    web application. 
    """
    return render_template("home.html"), 200


if __name__ == "__main__":
    app.run()
