from config.dbconfig import pg_config
from flask import jsonify
import psycopg2


class ImagesDAO:

  def __init__(self):
    connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'], pg_config['host'])

    self.conn = psycopg2._connect(connection_url)

  def insertImage(self, image_file, p_with_image):
    cursor = self.conn.cursor()
    cursor.execute("insert into instachat.image(image_file, p_with_image) "
                   "values(%s, %s) returning image_id;",
                   [image_file, p_with_image])
    image_id = cursor.fetchone()[0]
    self.conn.commit()
    return image_id
