#Veremos como valida una contraseña, usando while true

usuario=input("Escribe tu usuario: ")
intentos=1
while True:
    password=input("Escribe tu contraseña: ")
    if password=="secreto123" or intentos==3:
        print("Acceso correcto")
        break #Salir
    else:
        intentos+=1
        print("Contraseña incorrecta, intente nuevamente") 

nombre="Luis" #Guarda el valor
nombre=="Luis" #Compara el valor guardado