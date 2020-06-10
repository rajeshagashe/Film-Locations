from utils.flask_utils import flaskrun
from main import create_app, init_api
import os

application = create_app()
application = init_api(application)

if __name__ == "__main__":
    flaskrun(application)
