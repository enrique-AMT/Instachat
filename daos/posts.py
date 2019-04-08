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
    cursor.execute("select * from instachat.post left outer join instachat.image on post_id = p_with_image left outer "
                   "join instachat.has_hashtag as hh on post_id = p_with_hashtag left outer join instachat.hashtag as h "
                   "on hh.hashtag_id=h.hashtag_id ;")

    result = []
    for row in cursor:
      result.append(row)
    return result

  def getPostById(self, post_id):
    cursor = self.conn.cursor()
    posts_list = self.getAllPosts()
    if len(posts_list) < post_id or post_id < 1:
        return jsonify(Error="Post not found."), 404
    cursor.execute("select * from instachat.post left outer join instachat.image on post_id = p_with_image left outer "
                   "join instachat.has_hashtag as hh on post_id = p_with_hashtag left outer join instachat.hashtag as h "
                   "on hh.hashtag_id=h.hashtag_id where post_id = %s;", [post_id])
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getChatPosts(self, chat_id):
    cursor = self.conn.cursor()
    cursor.execute("select * from instachat.post left outer join instachat.image on post_id = p_with_image left outer "
                   "join instachat.has_hashtag as hh on post_id = p_with_hashtag left outer join instachat.hashtag as h "
                   "on hh.hashtag_id=h.hashtag_id where c_post_belongs = %s;", [chat_id])
    result = []
    for row in cursor:
      result.append(row)
    return result


  def getPostsInChatX(self, chat_id, post_id):
    cursor = self.conn.cursor()
    cursor.execute("select * from instachat.post left outer join instachat.image on post_id = p_with_image left outer "
                   "join instachat.has_hashtag as hh on post_id = p_with_hashtag left outer join instachat.hashtag as h "
                   "on hh.hashtag_id=h.hashtag_id where c_post_belongs = %s and post_id = %s;", [chat_id, post_id])
    result = cursor.fetchone()
    return result

  def getDailyPosts(self):
    cursor = self.conn.cursor()
    cursor.execute("select post_date, count(post_id) from instachat.post group by post_date")
    result = []
    for row in cursor:
      result.append(row)
    return result
