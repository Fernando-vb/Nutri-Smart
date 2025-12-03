from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User, UserCreate, Token
# In a real app, you'd have a service to handle business logic
# from services.auth_service import create_user, authenticate_user, create_access_token

router = APIRouter()

# Mock user database for demonstration
MOCK_USERS_DB = {}

@router.post("/register", response_model=User)
async def register(user_in: UserCreate):
    """
    Register a new user.
    """
    if user_in.email in MOCK_USERS_DB:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    # In a real app, you would hash the password
    hashed_password = user_in.password + "-hashed"
    user_db = User(
        _id=str(len(MOCK_USERS_DB) + 1),
        email=user_in.email,
        name=user_in.name,
    )
    MOCK_USERS_DB[user_in.email] = {"user": user_db.dict(), "password": hashed_password}
    
    return user_db

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate user and return a token.
    """
    user_in_db = MOCK_USERS_DB.get(form_data.username)
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # In a real app, you would verify the hashed password
    is_password_correct = (form_data.password + "-hashed") == user_in_db["password"]
    if not is_password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # In a real app, you would create a real JWT token
    access_token = f"{user_in_db['user']['email']}-fake-jwt-token"
    
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "user": user_in_db["user"]
    }
