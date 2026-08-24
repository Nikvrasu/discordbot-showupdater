from sqlalchemy import Column, Integer, ForeignKey

from db.database import Base


class UserShow(Base):
    __tablename__ = "user_shows"

    user_id = Column(Integer, primary_key=True)
    show_id = Column(Integer, primary_key=True)
    
    def __repr__(self):
        return f"<UserShow(user_id={self.user_id}, show_id={self.show_id})>"