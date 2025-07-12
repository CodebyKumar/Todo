"""
Test script for Todo API
Can be run standalone or with pytest
"""
import pytest
import requests
import json
from fastapi.testclient import TestClient
from app.main import app

# Test client for FastAPI
client = TestClient(app)

def test_health_endpoint():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to Todo API" in response.json()["message"]

def test_create_todo():
    """Test creating a new todo"""
    todo_data = {
        "title": "Test Todo",
        "description": "This is a test todo",
        "completed": False
    }
    response = client.post("/todos/", json=todo_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == todo_data["title"]
    assert data["description"] == todo_data["description"]
    assert data["completed"] == todo_data["completed"]
    assert "id" in data
    return data["id"]

def test_get_todos():
    """Test getting all todos"""
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_full_crud_workflow():
    """Test complete CRUD workflow"""
    # Create
    todo_data = {
        "title": "Test CRUD Todo",
        "description": "Testing CRUD operations",
        "completed": False
    }
    
    create_response = client.post("/todos/", json=todo_data)
    assert create_response.status_code == 200
    todo_id = create_response.json()["id"]
    
    # Read
    get_response = client.get(f"/todos/{todo_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == todo_data["title"]
    
    # Update
    update_data = {"completed": True}
    update_response = client.put(f"/todos/{todo_id}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["completed"] == True
    
    # Delete
    delete_response = client.delete(f"/todos/{todo_id}")
    assert delete_response.status_code == 200
    
    # Verify deletion
    get_deleted_response = client.get(f"/todos/{todo_id}")
    assert get_deleted_response.status_code == 404

# Manual test function (for running without pytest)
def manual_test_api():
    """Manual test for running against a live server"""
    BASE_URL = "http://localhost:8000"
    
    print("Testing Todo API...")
    
    # Test health endpoint
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Health check: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Server not running: {e}")
        return
    
    # Test create todo
    todo_data = {
        "title": "Manual Test Todo",
        "description": "This is a manual test todo",
        "completed": False
    }
    
    response = requests.post(f"{BASE_URL}/todos/", json=todo_data)
    print(f"Create todo: {response.status_code} - {response.json()}")
    
    if response.status_code == 200:
        todo_id = response.json()["id"]
        
        # Test get all todos
        response = requests.get(f"{BASE_URL}/todos/")
        print(f"Get all todos: {response.status_code} - Found {len(response.json())} todos")
        
        # Test get specific todo
        response = requests.get(f"{BASE_URL}/todos/{todo_id}")
        print(f"Get todo {todo_id}: {response.status_code} - {response.json()['title']}")
        
        # Test update todo
        update_data = {"completed": True}
        response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=update_data)
        print(f"Update todo: {response.status_code} - Completed: {response.json()['completed']}")
        
        # Test delete todo
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        print(f"Delete todo: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    # Run manual tests if executed directly
    manual_test_api()
