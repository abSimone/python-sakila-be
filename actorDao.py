from mysqlcon.db_utility import MySql
from typing import cast


class ActorDao:
    def findAllActors(self):
        MySql.openConnection()
        MySql.query("""SELECT * FROM Actor LIMIT 10""")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    def findFirstNameAndLastnameByFilmTitle(self, filmTitle):
        MySql.openConnection()
        MySql.query(f"SELECT a.first_name, a.last_name \
                      FROM Actor a, Film f, Film_Actor fa \
                      WHERE a.actor_id = fa.actor_id AND fa.film_id = f.film_id \
                      AND f.title = {filmTitle}")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

a = ActorDao()
for item in cast(list, a.findAllActors()):
  print(item)

