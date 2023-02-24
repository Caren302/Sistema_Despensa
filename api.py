import requests  #Importamos la librería requests


URL = "http://localhost/Ayuda_violeta/conexion.php" #configuramos la url
#solicitamos la información y guardamos la respuesta en data.
data = requests.get(URL) 

data = data.json() #convertimos la respuesta en dict



#print("Lista de Oficiales:")
#for element in data:
    #iteramos sobre data
    #print("Nombre:",element["nombre"],"Adscripcion",element["adscripcion"]) #Accedemos a sus valores
