import mysql.connector

class Productos:         
    def insert():
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="productos"
        )
        mycursor = mydb.cursor()
        
        sql = "INSERT INTO productos (sku,nombre_producto,unidad) VALUES (%s, %s,%s)"
        productos=("75362728384646","Sangia Casera 600ml","piezas (Pz)")

        mycursor.execute(sql, productos)
        mydb.commit()

        print(mycursor.rowcount, "producto(s) insertador")
        
    def select():
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="productos"
      )
      mycursor = mydb.cursor()

      mycursor.execute("SELECT * FROM productos")

      myresult = mycursor.fetchall()

      for a in myresult:
        print(a)

      mydb.close()
        
        
    def delete():
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="productos "
        )
        mycursor = mydb.cursor()

        sql = "DELETE FROM productos WHERE sku = '345678934'"

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, "Producto(s) eliminados")


    def update():
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="productos"
      )

      mycursor = mydb.cursor()

      sql = "UPDATE productos SET unidad = '30 piezas (Pz)' WHERE sku = '364846869'" 

      mycursor.execute(sql)

      mydb.commit()

      print(mycursor.rowcount, "Productos actualizados")
        
    update()
    delete()
    delete()
    insert()
    select()
