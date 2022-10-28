import mysql.connector as mysql
import json
import os
# from pathlib import WindowsPath
from pathlib import Path
class MySql:

  @classmethod
  def openConnection(cls):
    config = json.loads(Path("./mysqlcon/c.json").read_text())
    # qui manca il dizionario da utilizzare come parametro per connect
    try:
      cls.conn =  mysql.connect(**config)
      cls.cursor = cls.conn.cursor()
    except mysql.Error as er:
      print("Connessione fallita...")
    finally:
      return cls.conn.cursor()
  
  @classmethod
  def query(cls, string):
    cls.cursor.execute(string)

  @classmethod
  def getResults(cls):
    return cls.cursor.fetchall()

  @classmethod
  def closeConnection(cls):
    cls.cursor.close()
    cls.conn.close()



