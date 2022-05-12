from mysql.connector import *
database_connection = connect(host="localhost",
                              database="student",
                              user="root",
                              password="chayanika@2508")
if database_connection.is_connected():
        db_Info = database_connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = database_connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute("select * from student")
        print(cursor.fetchall())
        # cursor.execute("create table description(hobbies varchar(30), programming varchar(40));")
        cursor.execute('''insert into description values("dancing, painting","C++, Python, Javascript")''')
        cursor.execute("select * from description;")
        print(cursor.fetchall())
        cursor.execute("show tables;")
        print(cursor.fetchall())

cursor.close()
database_connection.close()