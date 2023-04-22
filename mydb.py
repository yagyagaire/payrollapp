import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Data@2021'
)

# prepare a cursor object
cursorObj = db.cursor()

#Create a Database
cursorObj.execute("CREATE DATABASE easypay")

print(cursorObj.execute("SHOW DATABASES"))

print("All Done!")