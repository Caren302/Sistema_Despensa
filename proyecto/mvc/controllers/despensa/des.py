import web
import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database= "el_ajolote_ahorrador"
        )
class Despensa:
    def GET(self):
        render = web.template.render("mvc/views/despensa")
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM despensa")
        resultao = mycursor.fetchall()
        return render.lista(resultao)
    def POST(self):
        mycursor = mydb.cursor()
        form=web.input()
        producto= form.producto
        cantidad= form.cantidad
        precio= form.precio
        sku= form.sku
        despensa=(producto,precio,sku,cantidad)
        sql = "INSERT INTO despensa ( productos, precio, sku, cantidad, fecha) VALUES (%s, %s, %s, %s, current_timestamp()) "
        mycursor.execute(sql,despensa)
        mydb.commit()
        raise web.seeother('/despensa') 
