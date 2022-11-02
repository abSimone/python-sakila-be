from dao.actorDao import ActorDao

class Actor:
    def __init__(self, nome, cognome):
        self.nome = nome.capitalize()
        self.cognome = cognome.capitalize()

    def __str__(self):
      return f'{"nome": {self.nome}, "cognome" : {self.cognome}}'

class ActorDto:

    @classmethod
    def getAllActors(cls):
        data = ActorDao.findAllActors()
        newList = []
        for lista in data:
            a = Actor(lista[0], lista[1])
            newList.append({"nome": a.nome, "cognome" : a.cognome})
        return newList

    @classmethod
    def getActorsForFilm(cls, titolo_film: str):
        data = ActorDao.findFirstNameAndLastnameByFilmTitle(titolo_film)
        newList = []
        for lista in data:
            a = Actor(lista[0], lista[1])
            newList.append(f'{"nome": {a.nome}, "cognome" : {a.cognome}}')
        return newList




