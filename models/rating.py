from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship


from config.database import Base


class Rating(Base):

    __tablename__ = "rating"

    mov_id = Column(Integer,primary_key = True)
    rev_id = Column(Integer)
    rev_stars = Column(Integer)
    num_o_ratings = Column(Integer)
  
    #movie_casts = relationship("MovieCast", back_populates = "movies")

