#Veremos el uso de la estructura repititiva TRUE

while True: #Mientra sea verdadero
    opcion=input("Escribe 'salir' para terminar el ciclo: ")
    if opcion.lower()== "salir":
    #Al escribir la palabra "salir" recien podras salir del ciclo
    #Mientras tanto podras escribir cuanto quieras
        break

print("Ahora estas libre ...")

nombre="Luis" #Asignamos o guardamos la palabra Luis en la variable

print(nombre)
print(nombre.upper()) #Lo imprime en Mayusculas
print(nombre.lower()) #Lo imprime en Minusculas