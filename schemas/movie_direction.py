from pydantic import BaseModel



class MovieDirection(BaseModel):
        dir_id: int
        mov_id: int
       

        class Config:
            schema_extra = {
                "example":{
                    "dir_id": 1,
                    "mov_id":1,
                    
                }
            }
