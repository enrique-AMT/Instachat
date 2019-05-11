from config.dbconfig import pg_config
from flask import jsonify
from daos.users import UsersDAO
import psycopg2


class ReplyDAO:

  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def insertReply(self, reply_text, p_replied, user_that_replied):
    cursor = self.conn.cursor()
    cursor.execute("insert into instachat.reply(reply_text, p_replied, user_that_replied) "
                   "values(%s, %s, %s) returning reply_id;",
                   [reply_text, p_replied, user_that_replied])
    reply_id = cursor.fetchone()[0]
    self.conn.commit()
    return reply_id

  def getAllReplies(self):
    cursor = self.conn.cursor()
    query = "select reply_id, reply_text, p_replied, user_that_replied, to_char(reply_date, 'MM-DD-YYYY HH:MIPM') from instachat.reply;"
    cursor.execute(query)
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getPostReplies(self, post_id):
    cursor = self.conn.cursor()
    cursor.execute("select reply_id, reply_text, p_replied, user_that_replied, to_char(reply_date, 'MM-DD-YYYY HH:MIPM')"
                   " from instachat.reply where p_replied = %s;", [post_id])
    result = []
    for row in cursor:
        result.append(row)
    return result

  def getReplyById(self, reply_id):
    cursor = self.conn.cursor()
    cursor.execute("select reply_id, reply_text, p_replied, user_that_replied, to_char(reply_date, 'MM-DD-YYYY HH:MIPM')"
                   " from instachat.reply where reply_id = %s;", [reply_id])
    result = cursor.fetchone()
    return result

  def getReplyByDate(self, reply_date):
    cursor = self.conn.cursor()
    cursor.execute("select reply_id, reply_text, p_replied, user_that_replied, to_char(reply_date, 'MM-DD-YYYY HH:MIPM')"
                   " from instachat.reply where to_char(reply_date, 'MM-DD-YYYY') = %s;", [reply_date])
    result = []
    if len(cursor) == 0:
        return jsonify(Error='No replies found on this date.'), 404
    else:
        for row in cursor:
            result.append(row)
    return result

  def getReactsOnReply(self, reply_id):
    cursor = self.conn.cursor()
    reply_list = self.getAllReplies()
    if len(reply_list) < reply_id or reply_id < 1:
        return jsonify(Error='Reply not found'), 404
    cursor.execute("select * from instachat.react natural inner join instachat.reply where reply_id = %s;",
                   [reply_id])
    result = []
    for row in cursor:
        result.append(row)
    return result

