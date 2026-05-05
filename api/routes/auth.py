from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from jose import jwt
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from api.schemas.user import TokenResponse, UserCreate, UserLogin, UserResponse
from api.models.user import User
from config.config import ALGORITHM, SECRET_KEY
from db.database import get_db

router = APIRouter()
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/auth/register", tags=["register"], response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with that email already exists")

    hashed_password = crypt_context.hash(user.password)
    new_user = User(username=user.username, email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/auth/login", tags=["login"], response_model=TokenResponse)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not crypt_context.verify(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    payload_dict = {"sub": str(db_user.id), "exp": datetime.now(timezone.utc) + timedelta(days=7)}
    access_token = jwt.encode(payload_dict, SECRET_KEY, algorithm=ALGORITHM)
    return TokenResponse(access_token=access_token, token_type="bearer")