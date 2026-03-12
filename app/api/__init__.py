from app.api.health import health_bp
from app.api.auth import auth_bp
from app.api.employees import employees_bp
from app.api.departments import departments_bp
from app.api.salaries import salaries_bp

def register_blueprints(app):
    """Register all API blueprints"""
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(employees_bp)
    app.register_blueprint(departments_bp)
    app.register_blueprint(salaries_bp)
