import mysql.connector
class Crud_tienda:
    def select():
         mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="violeta"
        )
         mycursor = mydb.cursor()
         sql = "INSERT INTO oficiales (nombre, apellido_paterno,apellido_materno,cargo_grado) VALUES (%s, %s,%s,%s)"
         val = (form.nombre, form.apellido_paterno,form.apellido_materno,form.cargo)
         mycursor.execute(sql, val)
         mydb.commit()
         mydb.close()

    select()
