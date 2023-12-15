from fastapi import APIRouter


auth_router = APIRouter(
    prefix="/auth", responses={400: {"descritpion": "Not found"}}, tags=["auth"]
)


@auth_router.get("/")
async def hello():
    """Hello world"""
    return {"message": "Hello World"}


@auth_router.post("/login")
async def login():
    """Login a user in"""
    return {"message": "Hello World"}


@auth_router.post("/token-refresh")
async def refresh_token():
    """Refresh token"""
    return {"message": "Hello World"}


@auth_router.post("/register")
async def signup():
    """register new user"""
    return {"message": "Hello World"}


@auth_router.post("/logout")
async def logout_user():
    """Log out user"""
    return {"message": "Hello World"}


@auth_router.post("/forgot-password")
async def forgot_password():
    """forgot password"""
    return {"message": "Hello World"}


@auth_router.post("/reset-password")
async def reset_password():
    """Reset password"""
    return {"message": "Hello World"}
