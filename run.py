"""
This file is to be used by vercel. 
kindly set environment variable and run by: flask run
"""

import os
from app import create_app

config_name = os.environ.get("FLASK_CONFIG") or "default"
app = create_app(config_name)

if __name__ == "__main__":
    app.run(port= app.config["FLASK_RUN_PORT"])