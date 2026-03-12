import pytest
from flask import jsonify

def test_get_employees(client, auth_headers):
    """Test getting all employees"""
    response = client.get('/api/v1/employees/', headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_employee(client, auth_headers):
    """Test creating a new employee"""
    data = {
        'FirstName': 'John',
        'LastName': 'Doe',
        'Gender': 'Male',
        'DateOfBirth': '1990-01-01'
    }
    response = client.post('/api/v1/employees/', 
                          json=data, 
                          headers=auth_headers)
    assert response.status_code == 201
    assert response.json['FirstName'] == 'John'
    assert response.json['LastName'] == 'Doe'
    assert 'EmployeeID' in response.json

def test_get_employee_by_id(client, auth_headers):
    """Test getting a specific employee"""
    # First create an employee
    data = {
        'FirstName': 'Jane',
        'LastName': 'Smith',
        'Gender': 'Female',
        'DateOfBirth': '1992-05-15'
    }
    create_response = client.post('/api/v1/employees/', 
                                 json=data, 
                                 headers=auth_headers)
    employee_id = create_response.json['EmployeeID']
    
    # Then get it by ID
    response = client.get(f'/api/v1/employees/{employee_id}', 
                         headers=auth_headers)
    assert response.status_code == 200
    assert response.json['FirstName'] == 'Jane'
    assert response.json['EmployeeID'] == employee_id

def test_update_employee(client, auth_headers):
    """Test updating an employee"""
    # First create an employee
    data = {
        'FirstName': 'Bob',
        'LastName': 'Johnson',
        'Gender': 'Male',
        'DateOfBirth': '1988-03-20'
    }
    create_response = client.post('/api/v1/employees/', 
                                 json=data, 
                                 headers=auth_headers)
    employee_id = create_response.json['EmployeeID']
    
    # Update the employee
    update_data = {'LastName': 'Williams'}
    response = client.put(f'/api/v1/employees/{employee_id}', 
                         json=update_data, 
                         headers=auth_headers)
    assert response.status_code == 200
    assert response.json['LastName'] == 'Williams'

def test_delete_employee(client, auth_headers):
    """Test deleting an employee"""
    # First create an employee
    data = {
        'FirstName': 'Alice',
        'LastName': 'Brown',
        'Gender': 'Female',
        'DateOfBirth': '1995-07-10'
    }
    create_response = client.post('/api/v1/employees/', 
                                 json=data, 
                                 headers=auth_headers)
    employee_id = create_response.json['EmployeeID']
    
    # Delete the employee
    response = client.delete(f'/api/v1/employees/{employee_id}', 
                           headers=auth_headers)
    assert response.status_code == 204
    
    # Verify it's gone
    get_response = client.get(f'/api/v1/employees/{employee_id}', 
                            headers=auth_headers)
    assert get_response.status_code == 404
