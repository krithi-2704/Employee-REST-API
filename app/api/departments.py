from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.department_service import DepartmentService
from app.errors import bad_request, not_found

departments_bp = Blueprint('departments', __name__, url_prefix='/api/v1/departments')
department_service = DepartmentService()

@departments_bp.route('/', methods=['GET'])
@jwt_required()
def get_departments():
    """Get all departments"""
    departments = department_service.get_all_departments()
    return jsonify([d.to_dict() for d in departments]), 200

@departments_bp.route('/<int:department_id>', methods=['GET'])
@jwt_required()
def get_department(department_id):
    """Get department by ID"""
    department = department_service.get_department_by_id(department_id)
    if not department:
        return not_found(f"Department with ID {department_id} not found")
    return jsonify(department.to_dict()), 200

@departments_bp.route('/', methods=['POST'])
@jwt_required()
def create_department():
    """Create a new department"""
    data = request.get_json()
    if not data:
        return bad_request("No data provided")
    
    try:
        department = department_service.create_department(data)
        return jsonify(department.to_dict()), 201
    except ValueError as e:
        return bad_request(str(e))

@departments_bp.route('/<int:department_id>', methods=['PUT'])
@jwt_required()
def update_department(department_id):
    """Update a department"""
    data = request.get_json()
    if not data:
        return bad_request("No data provided")
    
    department = department_service.update_department(department_id, data)
    if not department:
        return not_found(f"Department with ID {department_id} not found")
    return jsonify(department.to_dict()), 200

@departments_bp.route('/<int:department_id>', methods=['DELETE'])
@jwt_required()
def delete_department(department_id):
    """Delete a department"""
    success = department_service.delete_department(department_id)
    if not success:
        return not_found(f"Department with ID {department_id} not found")
    return '', 204
