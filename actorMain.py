from fastapi import FastAPI
from dto.actorDto import ActorDto

app = FastAPI()

@app.get('/')
def getAllActors():
  return {"actors" : ActorDto.getAllActors()}

@app.get('/{filmtitle}')
def getActorsForFilm(filmtitle:str):
  return {"actors" : ActorDto.getActorsForFilm(filmtitle)}