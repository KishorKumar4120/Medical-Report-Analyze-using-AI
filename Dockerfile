# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port
EXPOSE 8000

# Run the FastAPI application using shell to resolve $PORT
CMD sh -c "uvicorn backend.app:app --host 0.0.0.0 --port $PORT"
