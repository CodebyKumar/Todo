from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate
from typing import List, Optional


class TodoService:
    @staticmethod
    def create_todo(db: Session, todo: TodoCreate) -> Todo:
        db_todo = Todo(
            title=todo.title,
            description=todo.description,
            completed=todo.completed
        )
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    @staticmethod
    def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
        return db.query(Todo).filter(Todo.id == todo_id).first()

    @staticmethod
    def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Todo]:
        return db.query(Todo).offset(skip).limit(limit).all()

    @staticmethod
    def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
        db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if db_todo:
            update_data = todo_update.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_todo, field, value)
            db.commit()
            db.refresh(db_todo)
        return db_todo

    @staticmethod
    def delete_todo(db: Session, todo_id: int) -> bool:
        db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if db_todo:
            db.delete(db_todo)
            db.commit()
            return True
        return False

    @staticmethod
    def get_completed_todos(db: Session) -> List[Todo]:
        return db.query(Todo).filter(Todo.completed == True).all()

    @staticmethod
    def get_pending_todos(db: Session) -> List[Todo]:
        return db.query(Todo).filter(Todo.completed == False).all()
