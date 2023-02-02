from pydantic import BaseModel



class MovieCast(BaseModel):
        act_id: int
        mov_id: int
        role: str
       

        class Config:
            schema_extra = {
                "example":{
                    "dir_id": 1,
                    "mov_id":1,
                    "role" : "Villano"
                    
                }
            }
