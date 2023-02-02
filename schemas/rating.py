from pydantic import BaseModel



class Rating(BaseModel):
        mov_id: int
        rev_id: int
        rev_stars: int
        num_o_ratings: int

       

        class Config:
            schema_extra = {
                "example":{
                    "mov_id": 1,
                    "rev_id": 1,
                    "rev_stars": 2,
                    "num_o_ratings": 3
                    
                }
            }
