from config.dbconfig import pg_config
from flask import jsonify
import psycopg2

class PostsDAO:
  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def getAllPosts(self):
    cursor = self.conn.cursor()
    cursor.execute("select * from instachat.post;")
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getPostById(self, post_id):
    cursor = self.conn.cursor()
    posts_list = self.getAllPosts()
    if len(posts_list) < post_id or post_id < 1:
        return jsonify(Error="Post not found."), 404
    cursor.execute("select * from instachat.post where post_id = %s;", [post_id])
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getChatPosts(self, chat_id):
    cursor = self.conn.cursor()
    cursor.execute("select post_id, post_caption, post_date, p_created_by" 
      " from instachat.post natural inner join instachat.hashtag"
      " where c_post_belongs= %s;",[chat_id])
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getPostsInChatX(self, chat_id):
    cursor = self.conn.cursor()
    cursor.execute("select post_id, post_caption, user_id from instachat.post natural inner join instachat.user "
                   "natural inner join instachat.chat where chat_id = %s and user_id in "
                   "(select p_created_by from instachat.chat where c_post_belongs = %s);",[chat_id, chat_id])

    # "select post_caption, hash_name, first_name, last_name, phone, u_email_address, post_date"
    # " from instachat.post natural inner join instachat.hashtag"
    # " natural inner join instachat.user natural inner join instachat.phone "
    # " where c_post_belongs= %s and post_id = %s;", [chat_id, post_id]

    result = cursor.fetchone()
    return result

  def getDailyPosts(self):
    cursor = self.conn.cursor()
    cursor.execute("select post_date, count(post_id) from instachat.post group by post_date")
    result = []
    for row in cursor:
      result.append(row)
    return result
