from utility.db import MySql


class ActorDao:
    @classmethod
    def findAllActors(cls):
        MySql.openConnection()
        MySql.query(
          "SELECT first_name, last_name \
           FROM Actor LIMIT 10\
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
    def findActorById(cls, id_attore):

      MySql.openConnection()
      MySql.query(f"SELECT first_name, last_name\
        FROM ACTOR\
          WHERE actor_id = {id_attore}")
      
      data = MySql.getResults()
          
      MySql.closeConnection()
      return data
