import mysql.connector

class Db_creador:
    def crear_db():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE el_ajolote_ahorrador")

    def tienda():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="el_ajolote_ahorrador"

        )
        mycursor = mydb.cursor()
        tiendas="""
      CREATE TABLE tiendas(
       id_tienda integer PRIMARY KEY AUTO_INCREMENT NOT NULL,
       nombre text,
       ubicacion text,
       descripcion text   
        );
        """

        mycursor.execute(tiendas)
        print(mycursor)
        
        
    def despensa():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database= "el_ajolote_ahorrador"

        )
        mycursor = mydb.cursor()
        des="""
        CREATE TABLE despensa(
       id_despensa integer  PRIMARY KEY AUTO_INCREMENT,
       productos varchar(50) ,
       fecha date,
       precio varchar(50),
       total varchar(50)   
        );
        """

        mycursor.execute(des)  
  
  
    #crear_db()
    #despensa()
    tienda()


#cd proyecto/mvc/models/db
#python3 dabase.py
# Descomentar variables en caso de que la db o tablas no se crean