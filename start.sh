#!/bin/bash
# Start script for Railway deployment

# Use PORT from environment, default to 8000
PORT=${PORT:-8000}

# Run uvicorn with the resolved port
exec uvicorn backend.app:app --host 0.0.0.0 --port $PORT
