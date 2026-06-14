from fastapi import APIRouter, Depends

from api.dependencies import get_current_user
from api.models.user import User


router = APIRouter()

@router.get("/users/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user