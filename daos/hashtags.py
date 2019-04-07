from config.dbconfig import pg_config
import psycopg2

class HashtagsDAO:
  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def getAllHashtags(self):
    cursor = self.conn.cursor()
    query = "select hash_name from instachat.hashtag;"
    cursor.execute(query)
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getHashtagById(self, hashtag_id):
    cursor = self.conn.cursor()
    cursor.execute("select hash_name from instachat.hashtag where hashtag_id = %s;", [hashtag_id])
    result = cursor.fetchone()
    return result

  def getDailyHashtags(self, post_date):
    cursor = self.conn.cursor()
    cursor.execute("select hash_name, count(hashtag_id) from instachat.hashtag natural inner join instachat.post natural inner join "
                   "instachat.has_hashtag where post_date = %s group by hash_name order by count(hashtag_id) desc;", [post_date])
    result = []
    for row in cursor:
      result.append(row)
    return result
