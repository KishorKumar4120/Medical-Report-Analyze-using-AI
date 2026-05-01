# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory to project root
WORKDIR /app

# Copy requirements first for better caching
COPY backend/requirements.txt ./backend/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend directory
COPY backend/ ./backend/

# Expose port
EXPOSE 8000

# Run uvicorn from backend directory
CMD ["sh", "-c", "cd backend && uvicorn app:app --host 0.0.0.0 --port 8000"]
