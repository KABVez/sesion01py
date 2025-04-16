#Sumaremos numeros hasta que el usuario ingrese un 0

suma=0 #Ira guardando la suma de numeros introducidos
contador=0 #Ira contando cuantos numeros hemos introducido

while True:
    numero=int(input("Ingresa un numero para sumarlo o 0 para salir: "))

    if numero==0:
        break
    suma+=numero #Suma, guarda lo que ya tiene mas el numero que va llegando
    print(f"La suma de los numeros es: {suma}")
    contador+=1
print(f"La suma de los numeros introducidos es: {suma}")
print(f"El usuario introdujo: {contador} numeros")