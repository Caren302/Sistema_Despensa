import web
import mysql.connector
import web

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Productos")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(mydb)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Productos (id INT AUTO_INCREMENT PRIMARY KEY, name, descripcion, sku")
mycursor = mydb.cursor()
sql = "INSERT INTO Productos (name, descripcion, sku ) VALUES (fabuloso, fabuloso,11111110)(colgate,paste de dientes, 151503025)"

mycursor.execute(sql)