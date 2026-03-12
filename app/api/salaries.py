from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.salary_service import SalaryService
from app.errors import bad_request, not_found

salaries_bp = Blueprint('salaries', __name__, url_prefix='/api/v1/salaries')
salary_service = SalaryService()

@salaries_bp.route('/', methods=['GET'])
@jwt_required()
def get_salaries():
    """Get all salaries"""
    salaries = salary_service.get_all_salaries()
    return jsonify([s.to_dict() for s in salaries]), 200

@salaries_bp.route('/employee/<int:employee_id>', methods=['GET'])
@jwt_required()
def get_salaries_by_employee(employee_id):
    """Get all salaries for a specific employee"""
    salaries = salary_service.get_salaries_by_employee(employee_id)
    return jsonify([s.to_dict() for s in salaries]), 200

@salaries_bp.route('/<int:salary_id>', methods=['GET'])
@jwt_required()
def get_salary(salary_id):
    """Get salary by ID"""
    salary = salary_service.get_salary_by_id(salary_id)
    if not salary:
        return not_found(f"Salary with ID {salary_id} not found")
    return jsonify(salary.to_dict()), 200

@salaries_bp.route('/', methods=['POST'])
@jwt_required()
def create_salary():
    """Create a new salary record"""
    data = request.get_json()
    if not data:
        return bad_request("No data provided")
    
    try:
        salary = salary_service.create_salary(data)
        return jsonify(salary.to_dict()), 201
    except ValueError as e:
        return bad_request(str(e))

@salaries_bp.route('/<int:salary_id>', methods=['PUT'])
@jwt_required()
def update_salary(salary_id):
    """Update a salary record"""
    data = request.get_json()
    if not data:
        return bad_request("No data provided")
    
    salary = salary_service.update_salary(salary_id, data)
    if not salary:
        return not_found(f"Salary with ID {salary_id} not found")
    return jsonify(salary.to_dict()), 200

@salaries_bp.route('/<int:salary_id>', methods=['DELETE'])
@jwt_required()
def delete_salary(salary_id):
    """Delete a salary record"""
    success = salary_service.delete_salary(salary_id)
    if not success:
        return not_found(f"Salary with ID {salary_id} not found")
    return '', 204
