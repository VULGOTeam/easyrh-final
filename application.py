import os

from flask import Flask, jsonify
from mongoengine import connect

from os.path import join, dirname
from dotenv import load_dotenv

from routes import Routes
from errors.InvalidUsage import InvalidUsage

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

application = Flask(__name__)

connect(host=os.environ["MONGO_URL"])


@application.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


Routes(application)

if __name__ == "__main__":
    application.config["DEBUG"] = True
    application.run()
