# Todo API

A modern, modular FastAPI backend for a Todo application with SQLite database.

## Features

- ✅ RESTful API with FastAPI
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Modular architecture (MVC pattern)
- ✅ Automatic API documentation (Swagger/OpenAPI)
- ✅ CORS support
- ✅ Pydantic data validation
- ✅ Service layer for business logic
- ✅ Database migrations ready

## Project Structure

```
abc/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app initialization
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py         # Database configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── todo.py            # SQLAlchemy models
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── todo.py            # Pydantic schemas
│   ├── routes/
│   │   ├── __init__.py
│   │   └── todo_routes.py     # API endpoints
│   └── services/
│       ├── __init__.py
│       └── todo_service.py    # Business logic
├── main.py                    # Application entry point
├── requirements.txt           # Dependencies
├── .env                      # Environment variables
├── start.sh                  # Startup script
└── README.md                 # This file
```

## Installation

1. **Clone or navigate to the project directory**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```
   
   Or use the startup script:
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

## API Endpoints

The API will be available at `http://localhost:8000`

### Todo Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /todos/` - Get all todos (with pagination)
- `POST /todos/` - Create a new todo
- `GET /todos/{todo_id}` - Get a specific todo
- `PUT /todos/{todo_id}` - Update a specific todo
- `DELETE /todos/{todo_id}` - Delete a specific todo
- `GET /todos/status/completed` - Get all completed todos
- `GET /todos/status/pending` - Get all pending todos

### API Documentation

Once the server is running, you can access:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Example Usage

### Create a Todo
```bash
curl -X POST "http://localhost:8000/todos/" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Buy groceries",
       "description": "Milk, eggs, bread",
       "completed": false
     }'
```

### Get All Todos
```bash
curl -X GET "http://localhost:8000/todos/"
```

### Update a Todo
```bash
curl -X PUT "http://localhost:8000/todos/1" \
     -H "Content-Type: application/json" \
     -d '{
       "completed": true
     }'
```

### Delete a Todo
```bash
curl -X DELETE "http://localhost:8000/todos/1"
```

## Data Model

### Todo
- `id`: Integer (Primary Key)
- `title`: String (Required)
- `description`: String (Optional)
- `completed`: Boolean (Default: False)
- `created_at`: DateTime (Auto-generated)
- `updated_at`: DateTime (Auto-updated)

## Architecture

This project follows a modular architecture:

- **Models**: SQLAlchemy ORM models for database entities
- **Schemas**: Pydantic models for request/response validation
- **Services**: Business logic layer
- **Routes**: API endpoint definitions
- **Database**: Database configuration and connection management

## Development

### Adding New Features

1. **Add new models** in `app/models/`
2. **Add corresponding schemas** in `app/schemas/`
3. **Implement business logic** in `app/services/`
4. **Create API routes** in `app/routes/`
5. **Register routes** in `app/main.py`

### Database

The SQLite database file (`todos.db`) will be created automatically when you first run the application.

## Environment Variables

Configure the application using the `.env` file:

- `DATABASE_URL`: Database connection string
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `DEBUG`: Debug mode (default: True)

## Deployment

### Deploy to Render

This project is configured for easy deployment to [Render](https://render.com):

1. **Fork/Clone this repository**

2. **Connect to Render:**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository

3. **Configure the service:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
   - **Environment:** `Python 3`

4. **Set Environment Variables (optional):**
   - `DEBUG=false` (for production)
   - The `PORT` environment variable is automatically set by Render

5. **Deploy:** Click "Create Web Service"

The application will automatically use Render's `PORT` environment variable and deploy successfully.

### Alternative Deployment Options

The project includes both `render.yaml` and `Procfile` for flexible deployment options:
- **render.yaml**: Native Render configuration
- **Procfile**: Compatible with Heroku and other platforms

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn
- Pydantic

See `requirements.txt` for the complete list of dependencies.
