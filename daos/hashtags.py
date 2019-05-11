from config.dbconfig import pg_config
import psycopg2

class HashtagsDAO:
  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def createHashtag(self, hash_name):
    cursor = self.conn.cursor()
    cursor.execute("insert into instachat.hashtag(hash_name) values (%s)  returning hashtag_id;", [hash_name])
    hashtag_id = cursor.fetchone()[0]
    self.conn.commit()
    return hashtag_id

  def insertHashtagToPost(self, post_id, hashtag_id):
    cursor = self.conn.cursor()
    cursor.execute("insert into instachat.has_hashtag(p_with_hashtag, hashtag_id)"
                   "values(%s, %s) returning (p_with_hashtag, hashtag_id);", [post_id, hashtag_id])
    self.conn.commit()
    return post_id

  def getAllHashtags(self):
    cursor = self.conn.cursor()
    query = "select * from instachat.hashtag;"
    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(row)
    return result

  def getHashtagById(self, hashtag_id):
    cursor = self.conn.cursor()
    cursor.execute("select hash_name, hashtag_id from instachat.hashtag where hashtag_id = %s;", [hashtag_id])
    result = cursor.fetchone()
    return result

  def getDailyHashtags(self, post_date):
    cursor = self.conn.cursor()
    cursor.execute("select hash_name, count(hashtag_id) from instachat.hashtag natural inner join instachat.post natural inner join "
                   "instachat.has_hashtag where to_char(post_date, 'MM-DD-YYYY') = %s group by hash_name order by count(hashtag_id) desc;", [post_date])
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getHashtahPostX(self, post_id):
    cursor = self.conn.cursor()
    cursor.execute("select hash_name, h.hashtag_id from instachat.post left outer join instachat.has_hashtag as hh on post_id= p_with_hashtag"
                   " left outer join instachat.hashtag as h on hh.hashtag_id = h.hashtag_id"
                   " where post_id = %s;", [post_id])
    result = []
    for row in cursor:
        result.append(row)
    return result;
