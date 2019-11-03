from psycopg2 import connect, OperationalError
username = "postgres"
passwd = "coderslab"
hostname = "127.0.0.1"  # lub "localhost"
db_name = "cinemas_db"
try:
    # tworzymy nowe połączenie
    cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
    print("Połączenie udane.")
    cnx.close()
except OperationalError:
    print("Nieudane połączenie.")