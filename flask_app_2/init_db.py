import psycopg2
from config import host, user, password, db_name
from traceback import format_exc

try:
    #connect to exist db
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True
    cursor = connection.cursor()

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "SELECT version();"
    #     )

    #     print(f"Server version: {cursor.fetchone()}")

    # # create new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             nick_name varchar(50) NOT NULL
    #         )"""
    #     )
    #     # connection.commit()
    #     print("[INFO] Table created successfully")
    
    # # insert data into a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (first_name, nick_name) 
    #         VALUES ('Oleg', 'Barracuda');"""
    #     )

    #     print("[INFO] Data was successfully inserted")
    
    # # get data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE first_name  = 'Oleg';"""
    #     )
    #     print(cursor.fetchone()) 
    
    # delete a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )
    #     print("[INFO] table was successfully deleted")
    with connection.cursor() as cursor:
        cursor.execute(open("schema.sql", "r").read())
        
    with connection.cursor() as cursor:

        cursor.execute(
            """INSERT INTO posts (title, content) VALUES ('First Post', 'Content for the first post');"""
        )
        cursor.execute(
            """INSERT INTO posts (title, content) VALUES ('Second Post', 'Content for the second post');"""
        )


except Exception as _ex:
    print(format_exc())
    print("[INFO] Errorr while working with PostgreSQL", _ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
