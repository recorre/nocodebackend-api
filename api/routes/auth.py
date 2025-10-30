"""
Authentication routes for the Comment Widget API.
"""
from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import structlog

from ..models import UserCreate, UserLogin
from ..dependencies import nocodebackend_request, hash_password, hash_email

router = APIRouter()
logger = structlog.get_logger()


@router.post("/register")
async def register(user: UserCreate) -> Dict[str, Any]:
    """Registra novo usuário"""
    data = {
        "name": user.name,
        "email": user.email,
        "password_hash": hash_password(user.password),
        "api_key": f"user_api_key_{user.email}",  # Generate a simple API key
        "plan_level": "free",
        "is_supporter": 0
    }

    result = await nocodebackend_request("POST", "create/users", data)

    # Retorna sem o password_hash
    return {
        "id": result.get("id") or result.get("data", {}).get("id"),
        "name": user.name,
        "email": user.email,
        "message": "User created successfully"
    }


@router.post("/login")
async def login(credentials: UserLogin) -> Dict[str, Any]:
    """Login do usuário (simplificado)"""
    print(f"DEBUG: Login attempt for email: {credentials.email}")

    try:
        # Busca usuário por email
        print("DEBUG: Fetching user from database")
        result = await nocodebackend_request(
            "GET",
            "read/users",
            params={"email": credentials.email}
        )
        print(f"DEBUG: Database result: {result}")

        users = result if isinstance(result, list) else result.get("data", [])
        print(f"DEBUG: Users found: {len(users) if users else 0}")

        if not users:
            print(f"DEBUG: No users found for email: {credentials.email}")
            logger.warning("login_attempt_failed", email=credentials.email, reason="user_not_found")
            raise HTTPException(status_code=401, detail="Invalid credentials")

        user = users[0]
        print(f"DEBUG: User found: {user.get('id')}")

        # Verifica senha
        expected_hash = hash_password(credentials.password)
        actual_hash = user.get("password_hash")
        print(f"DEBUG: Password check - expected: {expected_hash}, actual: {actual_hash}")

        if actual_hash != expected_hash:
            print("DEBUG: Password mismatch")
            logger.warning("login_attempt_failed", email=credentials.email, reason="invalid_password")
            raise HTTPException(status_code=401, detail="Invalid credentials")

        print("DEBUG: Login successful")
        # Em produção, gerar JWT token aqui
        return {
            "user_id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "message": "Login successful"
        }

    except Exception as e:
        print(f"DEBUG: Login exception: {type(e).__name__}: {str(e)}")
        import traceback
        print(f"DEBUG: Traceback: {traceback.format_exc()}")
        raise