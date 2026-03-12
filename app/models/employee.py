from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Employee:
    EmployeeID: Optional[int] = field(default=None, compare=False)
    FirstName: str
    LastName: str
    Gender: str
    DateOfBirth: str  # ISO format: YYYY-MM-DD
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'EmployeeID': self.EmployeeID,
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'Gender': self.Gender,
            'DateOfBirth': self.DateOfBirth
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Employee from dictionary"""
        return cls(
            EmployeeID=data.get('EmployeeID'),
            FirstName=data['FirstName'],
            LastName=data['LastName'],
            Gender=data['Gender'],
            DateOfBirth=data['DateOfBirth']
        )
