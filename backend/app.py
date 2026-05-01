from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
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

# Serve the index.html file at root
INDEX_HTML_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "index.html")

@app.get("/")
async def read_root():
    return FileResponse(INDEX_HTML_PATH)
