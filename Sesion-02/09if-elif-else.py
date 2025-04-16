#Crearemos un programa que con base al peso dado, emitira un dictamen
peso=float(input("Escribe tu peso  corporal: "))

if peso>120:
    print("Tienes sobrepeso")
elif peso<=120 and peso>=90:
    print("Eres corpulento")
elif peso<=90 and peso>=70:
    print("Eres fornido")
elif peso<=70 and peso>=50:
    print("Estas en forma")
elif peso<=50 and peso>=40:
    print("Eres delgado")
elif peso<=40 and peso>=20:
    print("Eres delgado")
else:
    print("Ese peso es insuficiente para un adulto")