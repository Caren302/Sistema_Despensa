import requests  #Importamos la librería requests
import web
import mysql.connector
    #iteramos sobre data
    #print("Nombre:",element["nombre"],"Adscripcion",element["adscripcion"]) #Accedemos a sus valores
urls = ("/", "Index")
app = web.application(urls, globals())
render = web.template.render("views/")
class Index:
    def GET(self):
        URL = "http://localhost/Ayuda_violeta/oficiales.php" #configuramos la url
        data = requests.get(URL)
        data = data.json() #convertimos la respuesta en dict 
        return render.index(data)
    def POST(self):
         form = web.input()
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
         raise web.seeother("/")
        
if __name__ == "__main__":
    app.run()    