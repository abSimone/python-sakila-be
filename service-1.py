
from dto.actorDto import ActorDto
from dto.filmDto import FilmDto

print(FilmDto().getAllFilms())
print(ActorDto().getAllActors())
print(ActorDto().getActorsById(1))
print(ActorDto().getActorsById(1))

# File service che effettuerà le invocazioni ai metodi del layer DTO

