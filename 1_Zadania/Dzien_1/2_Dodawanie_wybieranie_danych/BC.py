from psycopg2 import connect, OperationalError
username = "postgres"
passwd = "coderslab"
hostname = "127.0.0.1"  # lub "localhost"
db_name = "postgres"
try:
    # tworzymy nowe połączenie
    cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
    cnx.autocommit = True
    print("Połączenie udane.")
    cursor = cnx.cursor()
    cursor.execute('Select * From cinema ')
    for i in cursor:
        print(i)
    # cursor.execute("""
# CREATE TABLE Product(
# id serial,
# name varchar(255),
# description text,
# price decimal(5,2),
# PRIMARY KEY (id)
# );
#
# CREATE TABLE “Order”(
# id serial,
# description text,
# PRIMARY KEY (id)
# );
#
# CREATE TABLE Client(
# id serial,
# name varchar(255),
# surname varchar(255),
# PRIMARY KEY (id)
# );
#     """)
    cnx.close()
except OperationalError as e:
    print(e)