#!/bin/bash
# Start script for Railway deployment

# Use Railway's PORT or default to 8000
export PORT=${PORT:-8000}

echo "Starting with PORT=$PORT"

# Run uvicorn with the resolved port
exec uvicorn backend.app:app --host 0.0.0.0 --port $PORT
