from dao.actorDao import ActorDao

class Actor:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
      return '{"nome": self.nome, "cognome" : self.cognome}'

class ActorDto:

    @classmethod
    def getAllActors(cls):
        data = ActorDao.findAllActors()
        newList = []
        for lista in data:
            newList.append(Actor(lista[0], lista[1]))
        return newList

    @classmethod
    def getActorsForFilm(cls, titolo_film: str):
        data = ActorDao.findFirstNameAndLastnameByFilmTitle(titolo_film)
        newList = []
        for lista in data:
            newList.append(Actor(lista[0], lista[1]))
        return newList


print(ActorDao.findAllActors())

