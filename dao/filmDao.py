from dao.utility.db import MySql

class Film:

    @classmethod
    def getAllFilm(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM film")
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllPgFilms(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM film WHERE rating like 'PG%'")
        
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllTitleStartR(cls):
        MySql.openConnection()
        MySql.query("SELECT title FROM film WHERE title LIKE 'R%'")

        data = MySql.getResults()
        MySql.closeConnection()

        return data