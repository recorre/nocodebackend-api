"""
Main entry point for the FastAPI backend application.
This file initializes the FastAPI app and includes all API routes.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# Import the API app from api/index.py
from api.index import app as api_app

# Use the API app as the main app
app = api_app

# Update app configuration for main entry point
app.title = "NoCodeBackend API"
app.description = "A FastAPI backend for NoCodeBackend with full API routes"
app.version = "1.0.0"

# Add additional CORS if needed (api/index.py already has CORS, but ensuring it's comprehensive)
if not any(isinstance(middleware, CORSMiddleware) for middleware in app.user_middleware):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Add main entry point if running directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)