from dao.actorDao import ActorDao


class Actor:
  def __init__(self, nome, cognome):
    self.nome = nome
    self.cognome = cognome


class ActorDto:

  @classmethod
  def getAllActors(cls):
    data = ActorDao.findAllActors()
    newDict = {}
    for i, lista in enumerate(data):
      newDict[i] = Actor(lista[0], lista[1])
    return newDict

  @classmethod
  def getActorsForFilm(cls, titolo_film: str):
    data = ActorDao.findFirstNameAndLastnameByFilmTitle(titolo_film)
    newDict = {}
    for i, lista in enumerate(data):
      newDict[i] = Actor(lista[0], lista[1])
    return newDict
