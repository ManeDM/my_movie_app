from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.actor import Actor
from config.database import Session
from service.actor import ActorService



actor_router = APIRouter()

@actor_router.get('/actors',tags=['actors'], response_model=Actor, status_code= 200)
def get_actor() ->Actor:   
    db = Session()
    result = ActorService(db).get_actors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@actor_router.get('/actors/{id}',tags=['actors'], response_model=List[Actor])
def get_actor(id:int) -> Actor:
    db = Session()
    result = ActorService(db).get_actor_by_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@actor_router.post('/actors{id}', tags=['actors'], status_code=201 , response_model=dict)
def create_actor(actor:Actor) ->dict:
    db= Session()
    ActorService(db).create_actor(actor)
    return JSONResponse(content={'message':'actor save in data base'})

@actor_router.put('/actors/{id}',tags=['actors'])
def update_actor(id:int,actor:Actor):
    db =  Session()
    result = ActorService(db).get_actor_by_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    ActorService(db).update_actor(id,actor)
    return JSONResponse(content={"message":"SActor has been modified"})

@actor_router.delete('/actors/delete_actor/',tags=['actors'])
def delete_movie(id:int):
    db = Session()
    result = ActorService(db).delete_actor(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content="Delete actor", status_code=200)
    

