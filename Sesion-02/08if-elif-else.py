#veremos un ejemplo de if-elif-else
calificacion=float(input("Ingresa tu calificacion: "))
if calificacion>=18 and calificacion<=20:
    print("felicitaciones, tienes una calificacion excelente ...")
elif calificacion>=11 and calificacion<=17.9:
    print("obtuviste una calificacion suficiente, esfuerzate mas")
elif calificacion>=10.9 and calificacion>=0:
    print("No te esforzaste lo suficiente, has reprobado el curso")
else: 
    print("Ingresa un numero valido")