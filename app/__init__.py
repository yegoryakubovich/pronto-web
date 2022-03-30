from flask import Flask
from flask_jwt_extended import JWTManager

from config import SECRET_KEY, DEBUG


blueprints = []


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['DEBUG'] = DEBUG

    JWTManager(app)

    [app.register_blueprint(blueprint) for blueprint in blueprints]
    return app
