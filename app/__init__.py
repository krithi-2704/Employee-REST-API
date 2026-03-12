from flask import Flask
from app.config import BaseConfig, DevelopmentConfig, TestingConfig, ProductionConfig
from app.extensions import jwt
from app.errors import register_error_handlers
from app.api import register_blueprints

# Config mapping for string-based config
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': BaseConfig
}

def create_app(config_object='default'):
    app = Flask(__name__)
    
    # Load config - handle both string and class
    if isinstance(config_object, str):
        # Get config class from mapping
        config_class = config_by_name.get(config_object, BaseConfig)
        app.config.from_object(config_class)
    else:
        # Direct config class
        app.config.from_object(config_object)

    # Initialize extensions
    jwt.init_app(app)

    # Register error handlers
    register_error_handlers(app)

    # Register blueprints
    register_blueprints(app)

    return app
