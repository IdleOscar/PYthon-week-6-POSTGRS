import psycopg2
from psycopg2 import OperationalError
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection(
 "postgres", "postgres", "123", "127.0.0.1", "5432"
)

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
 id SERIAL PRIMARY KEY,
 name TEXT NOT NULL,
 age INTEGER,
 gender TEXT,
 nationality TEXT
)
"""
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
execute_query(connection, create_users_table)

insert_query = (
f"INSERT INTO users (name, age, gender, nationality) VALUES {'Aliaskar',19,'male','KZ'}"
)
connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query)