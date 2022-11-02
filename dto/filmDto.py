from dao.filmDao import Film

class FilmName:
    def __init__(self, titolo):
        self.titolo = titolo

class FilmDto:

    @classmethod
    def getAllFilms(cls):
        data = Film.getAllFilm()
        newList = []
        for lista in data:
            newList.append(FilmName(lista[1]))
        return newList
