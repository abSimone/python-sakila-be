from utility.db import MySql

class Film:

    @classmethod
    def getAllFilm(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM film")
        data = MySql.getResults()
        MySql.closeConnection()

        return data