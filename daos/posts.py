from config.dbconfig import pg_config
from flask import jsonify
import psycopg2
from daos.chats import ChatsDAO

class PostsDAO:
  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def getAllPosts(self, chat_id):
    cursor = self.conn.cursor()
    cursor.execute("select post_caption, hash_name, first_name, last_name, phone, u_email_address, post_date" 
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

  def getUsersThatReact(self, post_id, react_type):
    cursor = self.conn.cursor()
    cursor.execute("select distinct user_id, first_name, last_name, react_date from instachat.post natural inner join "
                   "instachat.react natural inner join instachat.user where react_type = %s and user_id in "
                   "(select user_that_reacted from instachat.react where p_reacted = %s);", [react_type, post_id])
    result = []
    for row in cursor:
        result.append(row)
    return result
