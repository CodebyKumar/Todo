from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine
from app.models.todo import Todo
from app.routes.todo_routes import router as todo_router

# Create database tables
Todo.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Todo API",
    description="A simple Todo API built with FastAPI and SQLite",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(todo_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
