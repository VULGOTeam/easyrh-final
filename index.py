import os

import flask
from mongoengine import connect

from os.path import join, dirname
from dotenv import load_dotenv

from routes import Routes
from errors.InvalidUsage import InvalidUsage

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

connect(host=os.environ.get("MONGO_URL"))


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = flask.jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


Routes(app)

app.run()
