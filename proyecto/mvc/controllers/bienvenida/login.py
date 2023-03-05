import web
import mysql.connector
render = web.template.render("mvc/views/")
class Login:
   def GET(self): 
        nombre='Roberto' 
        return render.login(nombre)
   def POST(self):
        form=dict(web.input())
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="el_ajolote_ahorrador"
          )
        mycursor = mydb.cursor(dictionary=True)

        sql="SELECT nombre,correo,contraseña FROM usuarios WHERE correo=%s and contraseña=%s"
        balu=(form['correo'],form['password'])
        mycursor.execute(sql,balu)
        myresult = mycursor.fetchall()

        for a in myresult:
           if a['correo']==form['correo'] and a['contraseña']== form['password']:
               return render.index(a)

        mydb.close()