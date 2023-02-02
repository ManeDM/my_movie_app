from sqlalchemy import Column, Integer, ForeignKey
#from sqlalchemy.orm import relationship

from config.database import Base

class MovieCast(Base):

    __tablename__ = "movie_cast"

    act_id = Column(Integer, ForeignKey("act.id"))
    mov_id = Column(Integer, ForeignKey("mov.id"))
    role = Column(str)