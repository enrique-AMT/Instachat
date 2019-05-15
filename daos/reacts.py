from config.dbconfig import pg_config
from flask import jsonify
import psycopg2

class ReactsDAO:

  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])
    self.conn = psycopg2._connect(connection_url)

  def insertReactP(self, react_type, user_that_react, p_reacted):
    cursor = self.conn.cursor()
    cursor.execute("insert into instachat.react(react_type, user_that_react, p_reacted) "
                   "values(%s, %s, %s) returning react_id;",
                   [react_type, user_that_react, p_reacted])
    react_id = cursor.fetchone()[0]
    self.conn.commit()
    return react_id

  def insertReactR(self, react_type, user_that_react, reply_reacted):
    cursor = self.conn.cursor()
    cursor.execute("insert into instachat.react(react_type, user_that_react, reply_reacted) "
                   "values(%s, %s, %s) returning react_id;",
                   [react_type, user_that_react, reply_reacted])
    react_id = cursor.fetchone()[0]
    self.conn.commit()
    return react_id

  def getAllReacts(self):
    cursor = self.conn.cursor()
    query = "select react_id, react_type, user_that_react, p_reacted, reply_reacted, to_char(react_date, 'MM-DD-YYYY HH:MIPM') from instachat.react;"
    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(row)
    return result

  def getReactById(self, react_id):
    cursor = self.conn.cursor()
    cursor.execute("select react_id, react_type, user_that_react, p_reacted, reply_reacted, to_char(react_date, 'MM-DD-YYYY HH:MIPM') "
                   "from instachat.react where react_id = %s;", [react_id])
    result = cursor.fetchone()
    return result

  def getReactByDate(self, react_date):
    cursor = self.conn.cursor()
    cursor.execute("select react_id, react_type, user_that_react, p_reacted, reply_reacted, to_char(react_date, 'MM-DD-YYYY HH:MIPM')"
                   " from instachat.react where to_char(react_date, 'MM-DD-YYYY') = %s;", [react_date])
    result = []
    for row in cursor:
        result.append(row)
    return result

  def getReactsOnPost(self, post_id, react_type):
    cursor = self.conn.cursor()
    cursor.execute("select p_reacted, count(*) from instachat.react where p_reacted = %s and react_type = %s "
                   "group by p_reacted;",[post_id, react_type])
    result = []
    for row in cursor:
        result.append(row)
    return result

  def getReactsOnReplies(self, reply_id, react_type):
    cursor = self.conn.cursor()
    cursor.execute("select reply_reacted, count(*) from instachat.react where reply_reacted = %s and react_type = %s "
                   "group by reply_reacted;",[reply_id, react_type])
    result = []
    for row in cursor:
        result.append(row)
    return result

  def getDailyLikes(self):
    cursor = self.conn.cursor()
    cursor.execute("select to_char(react_date, 'MM-DD-YYYY'), react_type, count(react_id) from instachat.react where "
                   "react_type='like' group by react_type, to_char(react_date, 'MM-DD-YYYY') order by "
                   "to_char(react_date, 'MM-DD-YYYY') asc;")
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getDailyDislikes(self):
    cursor = self.conn.cursor()
    cursor.execute("select to_char(react_date, 'MM-DD-YYYY'), react_type, count(react_id) from instachat.react where "
                   "react_type='dislike' group by react_type, to_char(react_date, 'MM-DD-YYYY') order by "
                   "to_char(react_date, 'MM-DD-YYYY') asc;")
    result = []
    for row in cursor:
      result.append(row)
    return result
