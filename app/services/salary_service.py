from app.repositories.json_repository import JsonRepository
from app.models.salary import Salary
from typing import List, Optional

class SalaryService:
    def __init__(self):
        self.repo = JsonRepository('data/salaries.json', Salary)
    
    def get_all_salaries(self) -> List[Salary]:
        """Get all salaries"""
        return self.repo.get_all()
    
    def get_salary_by_id(self, salary_id: int) -> Optional[Salary]:
        """Get salary by ID"""
        return self.repo.get_by_id(salary_id)
    
    def get_salaries_by_employee(self, employee_id: int) -> List[Salary]:
        """Get all salaries for a specific employee"""
        all_salaries = self.get_all_salaries()
        return [s for s in all_salaries if s.EmployeeID == employee_id]
    
    def create_salary(self, data: dict) -> Salary:
        """Create a new salary record"""
        # Validate required fields
        required_fields = ['EmployeeID', 'BasicSalary', 'Bonus', 'Allowances']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        # Create salary
        salary = Salary.from_dict(data)
        return self.repo.create(salary)
    
    def update_salary(self, salary_id: int, data: dict) -> Optional[Salary]:
        """Update an existing salary record"""
        salary = self.get_salary_by_id(salary_id)
        if not salary:
            return None
        
        # Update fields
        if 'EmployeeID' in data:
            salary.EmployeeID = data['EmployeeID']
        if 'BasicSalary' in data:
            salary.BasicSalary = data['BasicSalary']
        if 'Bonus' in data:
            salary.Bonus = data['Bonus']
        if 'Allowances' in data:
            salary.Allowances = data['Allowances']
        
        return self.repo.update(salary_id, salary)
    
    def delete_salary(self, salary_id: int) -> bool:
        """Delete a salary record"""
        return self.repo.delete(salary_id)
