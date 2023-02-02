from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.movie import Movie as MovieModel
from service.actor import ActorService
from service.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()




#@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
@movie_router.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movies() -> Movie:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.get('/movies/{id}',tags=['movies'], response_model=List[Movie])
def get_movie(id:int) -> Movie:
    db = Session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.get('/movies/title/',tags=['movies'], response_model=dict)
def get_movie(title: str) ->dict:
    db = Session()
    result = MovieService(db).get_movie_by_title(title)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.post('/movies',tags=['movies'],status_code=201,response_model=dict)
def create_movie(movie:Movie)->dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message":"Se ha registrado la pelicula","status_code":201})

@movie_router.put('/movies/{id}',tags=['movies'])
def update_movie(id:int,movie:Movie):
    db =  Session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    MovieService(db).update_movie(id,movie)
    return JSONResponse(content={"message":"Se ha modificado la pelicula con id: {id}"})

@movie_router.delete('/movies/{id}',tags=['movies'])
def delete_movie(id:int):
    db = Session()
    result = ActorService(db).delete_actor(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content="Delete movie", status_code=200)
    