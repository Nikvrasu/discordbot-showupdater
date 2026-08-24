from fastapi import APIRouter, Depends

from api.dependencies import get_current_user
from api.models.user import User
from api.schemas.user import UserResponse


router = APIRouter()

@router.get("/users/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user