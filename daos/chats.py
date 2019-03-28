from config.dbconfig import pg_config
import psycopg2

class ChatsDAO:
  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def getAllChats(self):
    cursor = self.conn.cursor()
    query = "select * from chats;"
    cursor.execute(query)
    result = []
    for row in cursor:
      result.append(row)
    return result
