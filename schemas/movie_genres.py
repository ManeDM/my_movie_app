from pydantic import BaseModel



class MovieGenres(BaseModel):
        movie_id: int
        gen_id: int
        
       

        class Config:
            schema_extra = {
                "example":{
                    "movie_id": 1,
                    "gen_id":1,
                    
                }
            }
