from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from api.models.user import User
from config.config import ALGORITHM, SECRET_KEY
from db.database import get_db
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(db : Session = Depends(get_db), token = Depends(oauth2_scheme)):
    print("Token received in dependency:", token)
    try:
        jwt_decode = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = jwt_decode.get("sub")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user