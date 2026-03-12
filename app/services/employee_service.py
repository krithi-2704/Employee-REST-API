from app.repositories.json_repository import JsonRepository
from app.models.employee import Employee
from typing import List, Optional

class EmployeeService:
    def __init__(self):
        self.repo = JsonRepository('data/employees.json', Employee)
    
    def get_all_employees(self) -> List[Employee]:
        """Get all employees"""
        return self.repo.get_all()
    
    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """Get employee by ID"""
        return self.repo.get_by_id(employee_id)
    
    def create_employee(self, data: dict) -> Employee:
        """Create a new employee"""
        # Validate required fields
        required_fields = ['FirstName', 'LastName', 'Gender', 'DateOfBirth']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        # Create employee (ID will be auto-assigned by repository)
        employee = Employee.from_dict(data)
        return self.repo.create(employee)
    
    def update_employee(self, employee_id: int, data: dict) -> Optional[Employee]:
        """Update an existing employee"""
        employee = self.get_employee_by_id(employee_id)
        if not employee:
            return None
        
        # Update fields
        if 'FirstName' in data:
            employee.FirstName = data['FirstName']
        if 'LastName' in data:
            employee.LastName = data['LastName']
        if 'Gender' in data:
            employee.Gender = data['Gender']
        if 'DateOfBirth' in data:
            employee.DateOfBirth = data['DateOfBirth']
        
        return self.repo.update(employee_id, employee)
    
    def delete_employee(self, employee_id: int) -> bool:
        """Delete an employee"""
        return self.repo.delete(employee_id)
