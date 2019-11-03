from psycopg2 import connect


cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
cnx.autocommit = True

sql = """CREATE TABLE users (user_id serial, user_name varchar(255),
         user_email varchar(255) UNIQUE, PRIMARY KEY(user_id))"""
try:
    cursor.execute(sql)
except:
# obsługa błędu
