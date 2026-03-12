from app.repositories.json_repository import JsonRepository
from app.models.department import Department
from typing import List, Optional

class DepartmentService:
    def __init__(self):
        self.repo = JsonRepository('data/departments.json', Department)
    
    def get_all_departments(self) -> List[Department]:
        """Get all departments"""
        return self.repo.get_all()
    
    def get_department_by_id(self, department_id: int) -> Optional[Department]:
        """Get department by ID"""
        return self.repo.get_by_id(department_id)
    
    def create_department(self, data: dict) -> Department:
        """Create a new department"""
        # Validate required fields
        required_fields = ['DepartmentName', 'Location']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        # Create department
        department = Department.from_dict(data)
        return self.repo.create(department)
    
    def update_department(self, department_id: int, data: dict) -> Optional[Department]:
        """Update an existing department"""
        department = self.get_department_by_id(department_id)
        if not department:
            return None
        
        # Update fields
        if 'DepartmentName' in data:
            department.DepartmentName = data['DepartmentName']
        if 'Location' in data:
            department.Location = data['Location']
        
        return self.repo.update(department_id, department)
    
    def delete_department(self, department_id: int) -> bool:
        """Delete a department"""
        return self.repo.delete(department_id)
