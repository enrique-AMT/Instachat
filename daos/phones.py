from config.dbconfig import pg_config
from flask import jsonify
import psycopg2


class PhonesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'], pg_config['host'])

        self.conn = psycopg2._connect(connection_url)

    def createPhone(self, u_phone, phone):
        cursor = self.conn.cursor()
        cursor.execute("insert into instachat.phone(u_phone, phone) "
                       "values(%s, %s) returning phone_id;",
                       [u_phone, phone])
        phone_id = cursor.fetchone()[0]
        self.conn.commit()
        return phone_id

    def getPhones(self):
        cursor = self.conn.cursor()
        query = "select * from instachat.phone;"

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPhoneById(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("select * from instachat.phone where u_phone = %s;", [user_id])

        result = cursor.fetchone()
        return result





