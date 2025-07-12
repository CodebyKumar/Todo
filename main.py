import uvicorn
import os
from app.main import app


def main():
    # Render automatically assigns PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    host = "0.0.0.0"
    debug = os.environ.get('DEBUG', 'true').lower() == 'true'
    
    print(f"Starting Todo API server on {host}:{port}...")
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=debug
    )


if __name__ == "__main__":
    main()
