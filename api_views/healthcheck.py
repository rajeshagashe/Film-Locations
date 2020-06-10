from flask import jsonify, Blueprint

healthcheck_blueprint = Blueprint('healthcheck_blueprint', __name__)

@healthcheck_blueprint.route('/', methods=["GET"])
def health_check():
    return jsonify({"Health_check": "Success", "Status": 200})
