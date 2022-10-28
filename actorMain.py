from fastapi import FastAPI
from dto.actorDto import ActorDto
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="http://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def getAllActors():
  return {"actors" : ActorDto.getAllActors()}

@app.get('/{titolo_film}')
def getActorsForFilm(titolo_film:str):
  return {"actors" : ActorDto.getActorsForFilm(titolo_film)}