import flask

from routes import Routes
from errors.InvalidUsage import InvalidUsage

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = flask.jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


Routes(app)

app.run()
