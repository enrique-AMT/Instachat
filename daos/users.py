from config.dbconfig import pg_config
from flask import jsonify
import psycopg2

class UsersDAO:
  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def getAllUsers(self):
    cursor = self.conn.cursor()
    query = "select * from instachat.user;"
    cursor.execute(query)
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getUserById(self, user_id):
    cursor = self.conn.cursor()
    cursor.execute("select user_id, first_name, last_name from instachat.user where user_id = %s;", [user_id])
    result = cursor.fetchone()
    return result

  def getUserContactList(self, user_id):
    cursor = self.conn.cursor()
    cursor.execute("select contact_id from instachat.user natural inner join instachat.u_contacts where user_id = %s;", [user_id])
    ids = []
    result = []
    for row in cursor:
      ids.append(row[0])
    for row in ids:
      cursor.execute("select user_id, first_name, last_name from instachat.user where user_id = %s;", [row])
      result.append(cursor.fetchone())
    return result
