#calcularemos el promedio de 3 calificaciones,
#en mi caso tratare de indicar cuantos alumnos mas hay
alumno=input("Alumno: ")

mat=float(input("Calificacion de matematicas: "))
fis=float(input("Calificacion de fisica: "))
quim=float(input("Calificacion de quimica: "))

promedio=(mat+fis+quim)/3

print("La nota promedio del alumno: ",alumno, "es: ",round(promedio,2))

#
#