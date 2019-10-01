from flask import Blueprint
from flask_restplus import Api


blueprint = Blueprint('api', __name__,  url_prefix='/api/v1')
api = Api(blueprint)