from config.dbconfig import pg_config
import psycopg2

connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
pg_config['passwd'], pg_config['host'])

conn = psycopg2._connect(connection_url)