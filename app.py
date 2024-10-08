# """
# feedbackpulse: Web app starts here.
# """

# import os
# from flask import Flask, render_template
# from app.routes.auth import auth_blueprint

# app = Flask(__name__)
# app.secret_key = os.getenv("FLASK_SECRET_KEY")
# app.register_blueprint(auth_blueprint)


# @app.route("/")
# def home():
#     """
#     Landing page of the app with GitHub OAuth login. This is to
#     make sure only teamshiksha github org members can use this
#     web application.
#     """
#     return render_template("home.html"), 200


# @app.route("/dashboard")
# def dashboard():
#     """
#     Landing page of the app with GitHub OAuth login. This is to
#     make sure only teamshiksha github org members can use this
#     web application.
#     """
#     return render_template("dashboard.html"), 200


# if __name__ == "__main__":
#     print(app.url_map)
#     app.run()

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=5000)