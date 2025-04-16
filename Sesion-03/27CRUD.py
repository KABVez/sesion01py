import os
import time
import mysql.connector

mydb=mysql.connector.connect(
    host=
    user="maexspec_clases"
    password="Amiguito1"
    database="maexspec_clases"
)

mycursor=mydb.cursor()

while True:
    print("--- Menu del sistema ---"
    "\n1. Insertar un producto"
    "\n2. Eliminar un producto"
    "\n3. Buscar un producto"
    "\n4. Modificar un producto"
    "\n5. Mostrar un producto"
    "\n6. Salir del sistema"
    )
    opcion=int(input("Elige una opcion del menu: "))

    if option==1:
        clave=input("Clave del producto")
        nombre=input("Nombre del producto: ")
        precio=float(input("Precio del producto: "))

        sql="INSERT INTO productos (clave,nombre,precio) VALUES(%s,%s,%s)"

        val=(clave,nombre,precio)

        mycursor.execute(sql,val)

        mydb.commit()
        print("Producto agregado al sistema...")
        time.sleep(2)
        os.system("cls")

        66.228.61.234