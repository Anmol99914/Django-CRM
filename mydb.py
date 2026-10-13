import mysql.connector

database = mysql.connector.connect(
    host = 'localHost',
    user = 'root',
    password = 'anmol',
    port = '3306'
)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE icon")

print("All done:)")