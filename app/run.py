import os
from app import create_app  # Import create_app from the app package

app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("FLASK_RUN_PORT", 8000))  # fallback to 8000 if not found
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    app.run(host=host, port=port)
