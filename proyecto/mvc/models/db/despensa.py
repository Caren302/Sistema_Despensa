import mysql.connector

class Despensa:
    def  insert():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database= "el_ajolote_ahorrador"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO despensa (productos, fecha, precio, total) VALUES (%s, %s, %s, %s)"
        despensa=("Coca-cola 600ml","2023-03-01", 10, 10)
        mycursor.execute(sql, despensa)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    def delete():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database= "el_ajolote_ahorrador"
        )
        mycursor = mydb.cursor()
        sql = "DELETE FROM despensa WHERE id_despensa = %s"
        despensa = (1,)
        mycursor.execute(sql, despensa)
        mydb.commit()
        print(mycursor.rowcount, "despensa eliminada")

    def update():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database= "el_ajolote_ahorrador"
        )
        mycursor = mydb.cursor()
        sql = "UPDATE despensa SET productos = %s WHERE id_despensa = %s"
        despensa = ("Fanta", 1)
        mycursor.execute(sql, despensa)
        mydb.commit()
        print(mycursor.rowcount, "despensa actualizada")
    def select():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database= "el_ajolote_ahorrador"
        )



    select()
    #insert()
    #delete()
    #update()
    