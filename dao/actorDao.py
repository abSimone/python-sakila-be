from dao.utility.db import MySql


class ActorDao:
    @classmethod
    def findAllActors(cls):
        MySql.openConnection()
        MySql.query(
          "SELECT first_name, last_name \
            FROM Actor\
            ORDER BY last_name"
          )
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def findFirstNameAndLastnameByFilmTitle(cls, titolo_film):
        MySql.openConnection()
        MySql.query(
          f"SELECT a.first_name, a.last_name \
            FROM Actor a, Film f, Film_Actor fa \
            WHERE a.actor_id = fa.actor_id AND fa.film_id = f.film_id \
            AND f.title = '{titolo_film}'"
            )
        data = MySql.getResults()
        MySql.closeConnection()
        return data
      
    @classmethod
    def findActorByName(cls, name):
        MySql.openConnection()
        MySql.query(
          f"SELECT * FROM Actor WHERE first_name = '{name}'"
          )
        data = MySql.getResults()
        MySql.closeConnection()
        return data
      
    @classmethod
    def findActorBySurname(cls, surname):
        MySql.openConnection()
        MySql.query(
          f"SELECT * FROM Actor WHERE last_name = '{surname}'"
          )
        data = MySql.getResults()
        MySql.closeConnection()
        return data  

    @classmethod
    def findActorById(cls, id_attore):
        MySql.openConnection()
        MySql.query(
          f"SELECT first_name, last_name\
            FROM ACTOR\
            WHERE actor_id = {id_attore}"
        )
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def findActorByIdentityNumber(cls, id):
        MySql.openConnection()
        MySql.query(
          f"SELECT first_name, last_name\
            FROM ACTOR\
            WHERE actor_id = {id}"
        )
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def findFirstNameAndLastnameBy15NumFilm(cls):
        MySql.openConnection()
        MySql.query(
          f"SELECT actor.first_name, actor.last_name, COUNT(film_actor.actor_id) AS Num \
            FROM actor \
            INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id\
            GROUP BY film_actor.actor_id\
            HAVING COUNT(film_actor.actor_id) > 15"
        )
        data = MySql.getResults()
        MySql.closeConnection()      
        return data
