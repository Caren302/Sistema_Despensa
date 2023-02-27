import mysql.connector

class Crud_tiendas:
    def crear_db():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE el_ajolote_ahorrador")
        print(mycursor)

    def crear_table():
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
        print(mycursor)


    crear_table()
    crear_db()

#cd proyecto/mvc/models







