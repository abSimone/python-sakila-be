from dto.actorDto import ActorDto
from dto.filmDto import FilmDto

print(FilmDto().getAllFilms())
print(ActorDto().getAllActors())
print(ActorDto().getActorsById(1))