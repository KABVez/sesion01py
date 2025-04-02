#Veremos un programa con estructura
#este programa tiene entrada, proceso y salida de datos
#el programa calcula el area de un triangulo

#Entrada de datos
    #pedir los datos para calcular el area del triangulo
    base=float(input("Ingresa la base del triangulo"))
    altura=float(input("Ingresa la altura del triangulo"))
#procesamiento de datos
    #ejecutar la formula para calcular el area del triangulo
    area=(base*altura)/2
#salida de datos
    #mostrar la informacion (el area del trinagulo al usuario)
        #V1
        print("El area del triangulo es:",area)
        #V2
        print(f"El area del triangulo es:{area}")
