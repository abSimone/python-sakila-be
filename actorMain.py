from fastapi import FastAPI
from dto.actorDto import ActorDto

app = FastAPI()

@app.get('/')
def getAllActors():
  return {"actors" : ActorDto.getAllActors()}

@app.get('/{titolo_film}')
def getActorsForFilm(titolo_film:str):
  return {"actors" : ActorDto.getActorsForFilm(titolo_film)}