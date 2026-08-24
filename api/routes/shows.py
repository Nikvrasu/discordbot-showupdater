from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi.params import Depends

from api.dependencies import get_current_user
from api.models.show import Show
from api.models.user import User
from api.schemas.show import ShowResponse
from api.models.user_show import UserShow
from db.database import get_db

router = APIRouter()

@router.post("/shows/{show_id}/add", tags=["shows"], response_model=ShowResponse)
async def add_show_to_user(show_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    show = db.query(Show).filter(Show.id == show_id).first()
    if not show:
        raise HTTPException(status_code=404, detail="Show not found")

    user_show = db.query(UserShow).filter(UserShow.user_id == current_user.id, UserShow.show_id == show_id).first()
    if user_show:
        raise HTTPException(status_code=400, detail="Show already added to user's list")

    new_user_show = UserShow(user_id=current_user.id, show_id=show_id)
    db.add(new_user_show)
    db.commit()
    return ShowResponse(id=show.id, title=show.title, description=show.description, release_year=show.release_year, platform=show.platform, poster_image_url=show.poster_image_url, external_id=show.external_id)

@router.get("/shows/my", tags=["shows"], response_model=list[ShowResponse])
async def get_user_shows(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return [ShowResponse(id=show.id, title=show.title, description=show.description, release_year=show.release_year, platform=show.platform, poster_image_url=show.poster_image_url, external_id=show.external_id) for show in current_user.shows]

@router.delete("/shows/{show_id}/remove", tags=["shows"])
async def remove_show_from_user(show_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user_show = db.query(UserShow).filter(UserShow.user_id == current_user.id, UserShow.show_id == show_id).first()
    if not user_show:
        raise HTTPException(status_code=404, detail="Show not found in user's list")

    db.delete(user_show)
    db.commit()
    return {"detail": "Show removed from user's list"}