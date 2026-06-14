from tokenize import String

from sqlalchemy import Column, Integer

from db.database import Base


class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    poster_image_url = Column(String, nullable=True)
    platform = Column(String, nullable=True)
    description = Column(String, nullable=True)
    release_year = Column(Integer, nullable=True)
    external_id = Column(String, unique=True, index=True, nullable=True)

    def __repr__(self):
        return f"<Show(id={self.id}, title='{self.title}', release_year={self.release_year})>"