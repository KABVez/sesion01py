#Libreria de python para usar tiempo
import time

#calcularemos el promedio de 3 calificaciones,
#en mi caso tratare de indicar cuantos alumnos mas hay
alumno=input("Alumno: ")

mat=float(input("Calificacion de matematicas: "))
fis=float(input("Calificacion de fisica: "))
quim=float(input("Calificacion de quimica: "))

promedio=(mat+fis+quim)/3

#Esta parte obligara al codigo a hacer una pausa
print("Procesando........")
time.sleep(3)

#Resultado
print("La nota promedio del alumno: ",alumno, "es: ",round(promedio,2))

#
#