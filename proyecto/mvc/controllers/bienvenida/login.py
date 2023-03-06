import web
import mysql.connector


render = web.template.render("mvc/views/")
form=dict(web.input())
class Login:
   def GET(self):
      a=""
      return render.login(a)

    
      
   def POST(self):
    try: 
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
                 web.seeother('/index')
    except Exception as e:
            
            return "Error"
    