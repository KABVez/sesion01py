#Crearemos un ejemplo del uso de la estructura selectiva
#El programa pedira la hora en formato de 24h e indicar el saludo
hora=int(input("Ingrsa la hora en formato de 24h: "))

if hora>=0 and hora<25:
    if hora<12:
        print("Buen dia .....")
    elif hora<=8:
        print("Buena Tarde .....")
    else:
        print("Buena noche .....")