#Interfaces graficas
import tkinter as tk

from tkinter import messagebox

def ventana_con_boton():

    ventana=tk.Tk()

    ventana.title("Ejemplo con boton")


    ventana.geometry("400x300+400+200")


    boton=tk.Button(ventana, text="Haz click",
                    command=lambda:messagebox.showinfo("Mensaje", "Boton Presionado"))
    boton.pack(pady=20)

    ventana.mainloop()

ventana_con_boton()
