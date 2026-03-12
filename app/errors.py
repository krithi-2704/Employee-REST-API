from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

def error_response(status_code, message=None):
    """Create a JSON error response"""
    payload = {
        'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error'),
        'code': status_code
    }
    if message:
        payload['message'] = message
    return jsonify(payload), status_code

def bad_request(message=None):
    """Return a 400 Bad Request error"""
    return error_response(400, message)

def not_found(message=None):
    """Return a 404 Not Found error"""
    return error_response(404, message)

def unauthorized(message=None):
    """Return a 401 Unauthorized error"""
    return error_response(401, message)

def forbidden(message=None):
    """Return a 403 Forbidden error"""
    return error_response(403, message)

def internal_server_error(message=None):
    """Return a 500 Internal Server Error"""
    return error_response(500, message)

def register_error_handlers(app):
    """Register error handlers for the app"""
    
    @app.errorhandler(400)
    def handle_bad_request(e):
        return bad_request(getattr(e, 'description', None))
    
    @app.errorhandler(401)
    def handle_unauthorized(e):
        return unauthorized(getattr(e, 'description', None))
    
    @app.errorhandler(403)
    def handle_forbidden(e):
        return forbidden(getattr(e, 'description', None))
    
    @app.errorhandler(404)
    def handle_not_found(e):
        return not_found(getattr(e, 'description', None))
    
    @app.errorhandler(500)
    def handle_internal_server_error(e):
        return internal_server_error(getattr(e, 'description', None))
