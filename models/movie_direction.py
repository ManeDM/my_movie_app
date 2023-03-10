from sqlalchemy import Column, Integer, ForeignKey
#from sqlalchemy.orm import relationship

from config.database import Base

class MovieDirection(Base):

    __tablename__ = "movie_direction"

    dir_id = Column(Integer, ForeignKey("dir.id"))
    mov_id = Column(Integer, ForeignKey("mov.id"))