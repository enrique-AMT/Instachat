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

  def getDetailedUsers(self):
    cursor = self.conn.cursor()
    query = "select user_id, first_name, last_name from instachat.user;"
    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(row)
    return result

  def getUserById(self, user_id):
    cursor = self.conn.cursor()
    cursor.execute("select user_id, first_name, last_name, u_email_address, u_password, username, phone from "
                   "instachat.user left outer join instachat.phone on user_id = u_phone where user_id = %s;", [user_id])
    result = cursor.fetchone()
    return result

  def getUserByUsername(self, username):
    cursor = self.conn.cursor()
    cursor.execute("select user_id, first_name, last_name, u_email_address, u_password, username, phone from "
                   "instachat.user left outer join instachat.phone on user_id = u_phone where username = %s;", [username])
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

  def getUserChats(self, user_id):
    cursor = self.conn.cursor()
    # cursor.execute("select chat_id, chat_name, owner_id from instachat.chat where chat_id in (select c_user_belongs from "
    #                "instachat.belongs where u_belongs = %s);", [user_id])
    cursor.execute("select distinct chat_id, chat_name, owner_id from instachat.belongs "
                   "natural inner join instachat.user natural inner join instachat.chat where user_id = %s "
                   "and chat_id in (select c_user_belongs from instachat.belongs where u_belongs = %s) "
                   "or chat_id in (select chat_id from instachat.chat where owner_id = %s);", [user_id, user_id, user_id])
    result = []
    for row in cursor:
        result.append(row)
    return result

  def createUser(self, first_name, last_name, u_email_address, u_password, username):
    cursor = self.conn.cursor()
    cursor.execute("insert into instachat.user(first_name, last_name, u_email_address, u_password, username) "
                   "values(%s, %s, %s, %s, %s) returning user_id;",
                   [first_name, last_name, u_email_address, u_password, username])
    user_id = cursor.fetchone()[0]
    self.conn.commit()
    return user_id

  def checkUsersOnChat(self, user_id, chat_id):
    cursor = self.conn.cursor()
    cursor.execute("select u_belongs from instachat.belongs where c_user_belongs = %s and u_belongs = %s;",
                   [chat_id, user_id])
    result = []
    for row in cursor:
        result.append(row)
    return result

  def removeUserFromChat(self, user_id, chat_id):
    cursor = self.conn.cursor()
    cursor.execute("delete from instachat.belongs where u_belongs = %s and c_user_belongs = %s", [user_id, chat_id])
    self.conn.commit()
    return user_id

  def checkUserContacts(self, u_id, contact_id):
    cursor = self.conn.cursor()
    cursor.execute("select user_id from instachat.u_contacts where user_id = %s and contact_of = %s",
                   [contact_id, u_id])
    result = []
    for row in cursor:
        result.append(row)
    return result

  def removeUserFromContacts(self, user_id, contact_id):
    cursor = self.conn.cursor()
    cursor.execute("delete from instachat.u_contacts where contact_of = %s and user_id = %s", [user_id, contact_id])
    self.conn.commit()
    return user_id

  def insertUserToContacts(self, u_id, contact_id):
    cursor = self.conn.cursor()
    cursor.execute("insert into instachat.u_contacts (user_id, contact_of) values (%s, %s);", [u_id, contact_id])
    self.conn.commit()
    return u_id

  def login(self, username, password):
    cursor = self.conn.cursor()
    cursor.execute("select user_id from instachat.user where username = %s and u_password = %s", [username, password])
    result = cursor.fetchone()
    return result

  def getActiveUsers(self):
    cursor = self.conn.cursor()
    cursor.execute("select distinct on (to_char(post_date, 'MM-DD-YYYY')) to_char(post_date, 'MM-DD-YYYY'), username, count(post_id) from instachat.user "
                   "natural inner join instachat.post where user_id=p_created_by group by username, "
                   "to_char(post_date, 'MM-DD-YYYY') order by to_char(post_date, 'MM-DD-YYYY') desc;")
    result_list = []
    for row in cursor:
      result_list.append(row)
    return result_list
