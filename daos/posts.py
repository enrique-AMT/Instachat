from config.dbconfig import pg_config
import psycopg2

class PostsDAO:
  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def getAllPosts(self):
    cursor = self.conn.cursor()
    cursor.execute("select post_id, post_caption, post_date, user_id"
                   " from instachat.post natural inner join instachat.user natural inner "
                   "join instachat.post_belongs;")
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getChatPosts(self, chat_id):
    cursor = self.conn.cursor()
    cursor.execute("select post_id, post_caption, post_date, user_id" 
      " from instachat.post natural inner join instachat.hashtag natural inner join instachat.has_hashtag natural inner "
      "join instachat.post_belongs natural inner join instachat.user natural inner join instachat.phone natural inner join"
      " instachat.creates where chat_id= %s;",[chat_id])
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getPostById(self, chat_id, post_id):
    cursor = self.conn.cursor()
    cursor.execute("select post_caption, hash_name, first_name, last_name, phone, u_email_address, post_date" 
      " from instachat.post natural inner join instachat.hashtag natural inner join instachat.has_hashtag natural inner "
      "join instachat.post_belongs natural inner join instachat.user natural inner join instachat.phone natural inner join"
      " instachat.creates where chat_id= %s and post_id = %s;",[chat_id, post_id])
    result = cursor.fetchone()
    return result

  def getDailyPosts(self):
    cursor = self.conn.cursor()
    cursor.execute("select post_date, count(post_id) from instachat.post group by post_date")
    result = []
    for row in cursor:
      result.append(row)
    return result
