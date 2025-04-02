#Infraestructura selectiva

#if     , SI
#else   , ENTONCES
#elif   , SI ENTONCES

nombre=input("Inserte su nombre: ")
edad=float(input("Escribe tu edad: "))

if edad>=18: #se ejecutara el codigo solo si la edad es mayor o igual a 18
    print(nombre,"tienes", edad, "años, si puedes votar")

print(nombre,"tienes", edad, "años, no puedes votar")