from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.employee_service import EmployeeService
from app.errors import bad_request, not_found

employees_bp = Blueprint('employees', __name__, url_prefix='/api/v1/employees')
employee_service = EmployeeService()

@employees_bp.route('/', methods=['GET'])
@jwt_required()
def get_employees():
    """Get all employees"""
    employees = employee_service.get_all_employees()
    return jsonify([e.to_dict() for e in employees]), 200

@employees_bp.route('/<int:employee_id>', methods=['GET'])
@jwt_required()
def get_employee(employee_id):
    """Get employee by ID"""
    employee = employee_service.get_employee_by_id(employee_id)
    if not employee:
        return not_found(f"Employee with ID {employee_id} not found")
    return jsonify(employee.to_dict()), 200

@employees_bp.route('/', methods=['POST'])
@jwt_required()
def create_employee():
    """Create a new employee"""
    data = request.get_json()
    if not data:
        return bad_request("No data provided")
    
    try:
        employee = employee_service.create_employee(data)
        return jsonify(employee.to_dict()), 201
    except ValueError as e:
        return bad_request(str(e))

@employees_bp.route('/<int:employee_id>', methods=['PUT'])
@jwt_required()
def update_employee(employee_id):
    """Update an employee"""
    data = request.get_json()
    if not data:
        return bad_request("No data provided")
    
    employee = employee_service.update_employee(employee_id, data)
    if not employee:
        return not_found(f"Employee with ID {employee_id} not found")
    return jsonify(employee.to_dict()), 200

@employees_bp.route('/<int:employee_id>', methods=['DELETE'])
@jwt_required()
def delete_employee(employee_id):
    """Delete an employee"""
    success = employee_service.delete_employee(employee_id)
    if not success:
        return not_found(f"Employee with ID {employee_id} not found")
    return '', 204
