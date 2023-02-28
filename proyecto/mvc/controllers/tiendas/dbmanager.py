import mysql.connector
import json
class Crud_tienda:         
    def insert():
         mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
      database="el_ajolote_ahorrador"
        )
         mycursor = mydb.cursor()
         #*********************************************************************************
         #lineas para insertr con web.py
         #sql = "INSERT INTO tiendas (nombre, ubicacion,descipcion) VALUES (%s, %s,%s,%s)"
         #val = (form.nombre, form.apellido_paterno,form.apellido_materno,form.cargo)
         #*******************************************************************************
         sql = "INSERT INTO tiendas (nombre, ubicacion,descripcion) VALUES (%s, %s,%s)"
         tiendas=("bodega","aya","tienda,verde")

         mycursor.execute(sql, tiendas)
         mydb.commit()

         print(mycursor.rowcount, "record inserted.")
    def select():
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="el_ajolote_ahorrador"
          )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM tiendas")

        myresult = mycursor.fetchall()
        #res = json.dumps(x)
        #print(res)

        for a in myresult:
          print(a)

        mydb.close()
    def delete():
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="el_ajolote_ahorrador"
          )
        mycursor = mydb.cursor()
        sql = "DELETE FROM tiendas WHERE id_tienda = '4'"

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, "Tienda(s) exterminadas :(")

        
    delete()
    #select()
