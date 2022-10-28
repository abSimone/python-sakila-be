from dao.actorDao import ActorDao


class ActorDto:

  @classmethod
  def getAllActors(cls):
    data = ActorDao.findAllActors()
    newDict = {}
    for i, lista in enumerate(data):
      newDict[i] = {"nome": lista[0], "cognome": lista[1]}
    return newDict

  @classmethod
  def getActorsForFilm(cls, filmtitle: str):
    data = ActorDao.findFirstNameAndLastnameByFilmTitle(filmtitle)
    newDict = {}
    for i, lista in enumerate(data):
      newDict[i] = {"nome": lista[0], "cognome": lista[1]}
    return newDict
