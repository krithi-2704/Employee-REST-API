from flask import Flask
from app.config import BaseConfig
from app.extensions import jwt
from app.errors import register_error_handlers
from app.api import register_blueprints

def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    jwt.init_app(app)

    # Register error handlers
    register_error_handlers(app)

    # Register blueprints
    register_blueprints(app)

    return app
