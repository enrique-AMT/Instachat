from config.dbconfig import pg_config
from flask import jsonify
import psycopg2

class UsersDAO:
  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def getAllUsers(self):
    cursor = self.conn.cursor()
    query = "select * from instachat.user;"
    cursor.execute(query)
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getUserById(self, user_id):
    cursor = self.conn.cursor()
    cursor.execute("select user_id, first_name, last_name, u_email_address, u_password, phone"
                   " from instachat.user natural inner join instachat.phone where user_id = %s and u_phone=%s;",
                   [user_id, user_id])
    result = cursor.fetchone()
    return result

  def getUserContactList(self, user_id):
    cursor = self.conn.cursor()
    cursor.execute("select user_id, first_name, last_name from instachat.user where user_id in (select user_id from"
                     " instachat.u_contacts where contact_of = %s);", [user_id])
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getUserChatList(self, user_id):
    cursor = self.conn.cursor()
    cursor.execute("select distinct chat_id, chat_name, owner_id from instachat.chat natural inner join instachat.belongs where "
                   "c_user_belongs = %s;", [user_id])
    result = []
    for row in cursor:
      result.append(row)
    return result

  def getUsersThatReact(self, post_id, react_type):
    cursor = self.conn.cursor()
    cursor.execute("select user_id, first_name, last_name, react_date from instachat.user as u left outer join "
                   "instachat.react on u.user_id = user_that_react where p_reacted = %s and react_type = %s and u.user_id in "
                   "(select user_that_react from instachat.react where p_reacted = %s and react_type = %s);",
                   [post_id, react_type, post_id, react_type])
    result = []
    for row in cursor:
        result.append(row)
    return result
