from hashlib import new
from dao.actorDao import ActorDao


class Actor:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome


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
    
    @classmethod
    def getActorByName(cls, name: str):
        data = ActorDao.findActorByName(name)
        newList = []
        for lista in data:
            newList.append(Actor(lista[0], lista[1]))
        return newList
    
    @classmethod
    def getActorBySurname(cls, surname: str):
        data = ActorDao.findActorBySurname(surname)
        newList = []
        for lista in data:
            newList.append(Actor(lista[0], lista[1]))
        return newList

    @classmethod
    def getAllActorId (cls):
        data = ActorDao.findActorById()
        newList = []
        for lista in data:
            newList.append(Actor(lista[0]))
        return newList
    @classmethod
    def getActorsFor10NumFilm(cls):
        data = ActorDao.findFirstNameAndLastnameBy10NumFilm()
        newList = []
        for lista in data:
            newList.append(Actor(lista[0], lista[1]))
        return newList
