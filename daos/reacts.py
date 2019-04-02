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
    chat_list = self.getAllReacts()
    if len(chat_list) < react_id or react_id < 1:
        return jsonify(Error='Reacts not found'), 404
    cursor.execute("select * from instachat.react where chat_id = %s;", [react_id])
    result = []
    for row in cursor:
        result.append(row)
    return result
