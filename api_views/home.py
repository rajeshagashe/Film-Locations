from flask import request, jsonify, abort, Blueprint, render_template

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=["GET"])
def homepage(name=None):
    '''renders homepage.'''
    return render_template('hello.html', name=name)
