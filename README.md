# FastAPI Initial Project

This project is a basic FastAPI application structured for scalability and maintainability.

## Project Structure

```
.
├── app
│   ├── api
│   │   └── routers
│   │       ├── general.py
│   │       ├── items.py
│   │       ├── models.py
│   │       └── users.py
│   ├── schemas
│   │   ├── item.py
│   │   └── model.py
│   └── main.py
├── requirements.txt
└── README.md
```

- **app/main.py**: The main FastAPI application file that ties everything together.
- **app/api/routers/**: This directory contains the API endpoints, split into multiple files by resource.
- **app/schemas/**: This directory contains the Pydantic models for request and response data.
- **requirements.txt**: The project dependencies.

## How to run the application

1.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the application:

    You can run the application using either `uvicorn` or `fastapi-cli`.

    **Using Uvicorn:**
    ```bash
    uvicorn app.main:app --reload
    ```

    **Using FastAPI CLI:**
    ```bash
    fastapi dev app/main.py
    ```
The application will be available at `http://127.0.0.1:8000`.

**Note on `__init__.py` files:**

The empty `__init__.py` files in the directories are there to mark them as Python packages. This allows us to use absolute imports within the application (e.g., `from app.api.routers import items`). 