from config.dbconfig import pg_config
from flask import jsonify
import psycopg2


class PostsDAO:

  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def insertPost(self, post_caption, p_created_by, c_post_belongs):
    cursor = self.conn.cursor()
    cursor.execute("insert into instachat.post(post_caption, p_created_by, c_post_belongs) "
                   "values(%s, %s, %s) returning post_id;",
                   [post_caption, p_created_by, c_post_belongs])
    post_id = cursor.fetchone()[0]
    self.conn.commit()
    return post_id

  def getAllPosts(self):
    cursor = self.conn.cursor()
    cursor.execute("select post_id, post_caption, to_char(post_date, 'MM-DD-YYYY HH:MIPM'), p_created_by, image_file, hash_name from instachat.post "
                   "left outer join instachat.image on post_id = p_with_image left outer join instachat.has_hashtag "
                   "as hh on post_id = p_with_hashtag left outer join instachat.hashtag as h "
                   "on hh.hashtag_id=h.hashtag_id order by post_date asc;")

    result = []
    for row in cursor:
      result.append(row)
    return result

  def getPostById(self, post_id):
    cursor = self.conn.cursor()
    posts_list = self.getAllPosts()
    # if len(posts_list) < post_id or post_id < 1:
    #     return jsonify(Error="Post not found."), 404
    cursor.execute("select post_id, post_caption, to_char(post_date, 'MM-DD-YYYY HH:MIPM'), p_created_by, image_file, hash_name  from instachat.post "
                   "left outer join instachat.image on post_id = p_with_image left outer join instachat.has_hashtag "
                   "as hh on post_id = p_with_hashtag left outer join instachat.hashtag as h "
                   "on hh.hashtag_id=h.hashtag_id where post_id = %s order by post_date asc;", [post_id])
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getChatPosts(self, chat_id):
    cursor = self.conn.cursor()
    cursor.execute("select post_id, post_caption, to_char(post_date, 'MM-DD-YYYY HH:MIPM'), p_created_by, image_file, "
                   "hash_name  from instachat.post left outer join instachat.image on post_id = p_with_image left outer "
                   "join instachat.has_hashtag as hh on post_id = p_with_hashtag left outer join instachat.hashtag as h "
                   "on hh.hashtag_id=h.hashtag_id where c_post_belongs = %s order by post_date asc;", [chat_id])
    result = []
    for row in cursor:
      result.append(row)
    return result


  def getPostsInChatX(self, chat_id, post_id):
    cursor = self.conn.cursor()
    cursor.execute("select post_id, post_caption, to_char(post_date, 'MM-DD-YYYY HH:MIPM'), p_created_by, image_file, "
                   "hash_name  from instachat.post left outer join instachat.image on post_id = p_with_image left outer "
                   "join instachat.has_hashtag as hh on post_id = p_with_hashtag left outer join instachat.hashtag as h "
                   "on hh.hashtag_id=h.hashtag_id where c_post_belongs = %s and post_id = %s order by post_date asc "
                   ";", [chat_id, post_id])
    result = cursor.fetchone()
    return result

  def getDailyPosts(self):
    cursor = self.conn.cursor()
    cursor.execute("select to_char(post_date, 'MM-DD-YYYY'), count(post_id) from instachat.post group by "
                   "to_char(post_date, 'MM-DD-YYYY')")
    result = []
    for row in cursor:
      result.append(row)
    return result
