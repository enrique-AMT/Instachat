from config.dbconfig import pg_config
from flask import jsonify
import psycopg2

class ChatsDAO:
  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def getAllChats(self):
    cursor = self.conn.cursor()
    query = "select * from instachat.chat;"
    cursor.execute(query)
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getChatById(self, chat_id):
    cursor = self.conn.cursor()
    chat_list = self.getAllChats()
    if len(chat_list) < chat_id or chat_id < 1:
      return jsonify(Error='Chat not found'), 404
    cursor.execute("select * from instachat.chat where chat_id = %s;", [chat_id])
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getChatPosts(self, chat_id):
    cursor = self.conn.cursor()
    chat_list = self.getAllChats()
    print(len(chat_list))
    if len(chat_list) < chat_id or chat_id < 1:
      return jsonify(Error='Chat not found'), 404
    cursor.execute("select * from instachat.post_belongs natural inner join instachat.post where chat_id = %s;", [chat_id])
    something = []
    something.append(cursor)
    print(len(something))
    result = []
    for row in cursor:
      result.append(row)
    return result
