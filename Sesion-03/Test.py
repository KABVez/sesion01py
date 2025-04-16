import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="66.228.61.234",  # o IP pública del servidor
        user="maexspec_clases",
        password="Amiguito1",
        database="maexspec_clases"
    )
    print("Conexión exitosa")
except mysql.connector.Error as err:
    print("Error al conectar:", err)