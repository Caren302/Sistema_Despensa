import mysql.connector
class Crud_tienda:
    def select():
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
         sql = "INSERT INTO tiendas (nombre, ubicacion,descipcion) VALUES (%s, %s,%s,%s)"
         tiendas=[
        ("Walmartk","aqui mero","tienda azul"),
        ("bodega ahorrera","aya mero","kilo (kl)"),
        ("75111005566789","camaron 200 gr","kilo(kl)"),


        ]
         mycursor.execute(sql, tiendas)
         mydb.commit()
         mydb.close()

    select()
