from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Department:
    DepartmentID: Optional[int] = field(default=None, compare=False)
    DepartmentName: str
    Location: str
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'DepartmentID': self.DepartmentID,
            'DepartmentName': self.DepartmentName,
            'Location': self.Location
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Department from dictionary"""
        return cls(
            DepartmentID=data.get('DepartmentID'),
            DepartmentName=data['DepartmentName'],
            Location=data['Location']
        )
