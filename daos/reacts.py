from config.dbconfig import pg_config
from flask import jsonify
import psycopg2

class ReactsDAO:

  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])
    self.conn = psycopg2._connect(connection_url)

  def getAllReacts(self):
    cursor = self.conn.cursor()
    query = "select * from instachat.react;"
    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(row)
    return result

  def getReactById(self, react_id):
    cursor = self.conn.cursor()
    cursor.execute("select * from instachat.react where react_id = %s;", [react_id])
    result = cursor.fetchone()
    return result

  def getReactByDate(self, react_date):
    cursor = self.conn.cursor()
    cursor.execute("select * from instachat.react where react_date = %s;", [react_date])
    result = []
    for row in cursor:
        result.append(row)
    return result

  def getReactsOnPost(self, post_id, react_type):
    cursor = self.conn.cursor()
    cursor.execute("select p_reacted, count(*) from instachat.react where p_reacted = %s and react_type = %s "
                   "group by p_reacted;",[post_id, react_type])
    result = []
    for row in cursor:
        result.append(row)
    return result
