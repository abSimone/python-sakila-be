from dao.mysql.db_utility import MySql
import json


class ActorDao:
    @classmethod
    def findAllActors(cls):
        MySql.openConnection()
        MySql.query("""SELECT first_name, last_name FROM Actor LIMIT 10""")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def findFirstNameAndLastnameByFilmTitle(cls, filmTitle):
        MySql.openConnection()
        MySql.query(f"SELECT a.first_name, a.last_name \
                      FROM Actor a, Film f, Film_Actor fa \
                      WHERE a.actor_id = fa.actor_id AND fa.film_id = f.film_id \
                      AND f.title = '{filmTitle}'")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

