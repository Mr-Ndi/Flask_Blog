import mysql.connector

my_db = mysql.connector.connect(
    host = 'localhost',
    user = 'Ninshuti',
    passwd = 'byasana'
)

my_robot = my_db.cursor()

my_robot.execute('SHOW DATABASES')

for db in my_robot:
    print(db)
