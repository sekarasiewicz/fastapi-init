.PHONY: help run-uvicorn run-fastapi

help:
	@echo "Available commands:"
	@echo "  run-uvicorn   - Run the application using Uvicorn"
	@echo "  run-fastapi   - Run the application using FastAPI CLI"

run-uvicorn:
	@echo "Running application with Uvicorn..."
	uvicorn app.main:app --reload

run-fastapi:
	@echo "Running application with FastAPI CLI..."
	fastapi dev app/main.py 