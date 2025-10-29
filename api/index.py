"""
FastAPI Proxy para NoCodeBackend
Deploy: Vercel - Versão Simplificada
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime
from typing import Dict, Any

# Load environment variables
from dotenv import load_dotenv
load_dotenv()  # Remove o path específico

# ========================
# APP CONFIGURATION
# ========================

app = FastAPI(
    title="Comment Widget Proxy API",
    description="Proxy para NoCodeBackend - Hackathon Edition",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========================
# INCLUDE ROUTE MODULES
# ========================

# Import route modules from api/routes/
from .routes import auth, comments, threads, widget, advanced

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])
app.include_router(threads.router, prefix="/threads", tags=["threads"])
app.include_router(widget.router, prefix="/widget", tags=["widget"])
app.include_router(advanced.router, prefix="/api", tags=["api"])

# ========================
# BASIC ROUTES
# ========================

@app.get("/")
async def root() -> Dict[str, Any]:
    """Root endpoint"""
    return {
        "service": "Comment Widget Proxy",
        "status": "online",
        "version": "1.0.0",
        "instance": os.getenv("INSTANCE", "41300_teste")
    }

@app.get("/health")
async def health_check() -> Dict[str, Any]:
    """Verifica se a API está funcionando"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database_url": bool(os.getenv("DATABASE_URL")),
        "redis_url": bool(os.getenv("REDIS_URL"))
    }

# ========================
# VERCEL EXPORT
# ========================

# Para Vercel, apenas exportar o app
# NÃO adicionar handler = app - isso pode causar conflitos