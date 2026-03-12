from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Salary:
    EmployeeID: int
    BasicSalary: float
    Bonus: float
    Allowances: float
    SalaryID: Optional[int] = field(default=None, compare=False)

    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'SalaryID': self.SalaryID,
            'EmployeeID': self.EmployeeID,
            'BasicSalary': self.BasicSalary,
            'Bonus': self.Bonus,
            'Allowances': self.Allowances
        }

    @classmethod
    def from_dict(cls, data):
        """Create Salary from dictionary"""
        return cls(
            EmployeeID=data['EmployeeID'],
            BasicSalary=data['BasicSalary'],
            Bonus=data['Bonus'],
            Allowances=data['Allowances'],
            SalaryID=data.get('SalaryID')
        )
