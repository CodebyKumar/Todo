from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.services.todo_service import TodoService
from typing import List

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo item"""
    return TodoService.create_todo(db=db, todo=todo)


@router.get("/", response_model=List[TodoResponse])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all todo items with pagination"""
    todos = TodoService.get_todos(db, skip=skip, limit=limit)
    return todos


@router.get("/{todo_id}", response_model=TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a specific todo item by ID"""
    db_todo = TodoService.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    """Update a specific todo item"""
    db_todo = TodoService.update_todo(db, todo_id=todo_id, todo_update=todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a specific todo item"""
    success = TodoService.delete_todo(db, todo_id=todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}


@router.get("/status/completed", response_model=List[TodoResponse])
def get_completed_todos(db: Session = Depends(get_db)):
    """Get all completed todo items"""
    return TodoService.get_completed_todos(db)


@router.get("/status/pending", response_model=List[TodoResponse])
def get_pending_todos(db: Session = Depends(get_db)):
    """Get all pending todo items"""
    return TodoService.get_pending_todos(db)
