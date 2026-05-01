from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import sys

# Add the current directory to sys.path to ensure modules can be found
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

try:
    from routes.analyze import router
except ModuleNotFoundError:
    # Fallback: try adding parent directory
    parent_dir = os.path.dirname(backend_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    from routes.analyze import router

app = FastAPI(title="Medical Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

# Root endpoint - returns API info
@app.get("/")
async def read_root():
    return JSONResponse({"message": "Medical Report Analyzer API", "status": "running"})
