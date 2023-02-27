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
       id_tienda integer PRIMARY KEY NOT NULL,
       nombre text,
       ubicacion text,
       descipcion text   
        );
        """

        mycursor.execute(tiendas)
        
        
    def despensa():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="el_ajolote_ahorrador"

        )
        mycursor = mydb.cursor()
        des="""
        CREATE TABLE despensa(
       id_despensa integer  PRIMARY KEY AUTO_INCREMENT,
       productos varchar(50) ,
       fecha date,
       precio int,
       total int   
        );
        """

        mycursor.execute(des)
        print(mycursor)    
  
    #tienda()
    #crear_db()
    despensa()

#cd proyecto/mvc/models