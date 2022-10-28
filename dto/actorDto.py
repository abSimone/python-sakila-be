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



# aggiungi su actor i 3 metodi per get actor by id, nome, cognome
# add lista attori su più di 15 film