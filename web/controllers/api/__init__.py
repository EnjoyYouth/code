from flask import Blueprint
route_api = Blueprint('api_page', __name__)

@route_api.route("/")
def index():
    return "Mina Api V1.0"