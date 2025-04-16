import tkinter as tk
from tkinter import messagebox

def etiquetas_y_texto():
    ventana=tk.Tk()
    ventana.title("Etiquetas y cuadro de texto")

    ventana.geometry("400x250")
    etiqueta=tk.Label(ventana,text="Ingresa tu nombre: ",
                        font=("Arial",12,"bold"),fg="blue")
    etiqueta.pack(pady=5)
                    
    entrada=tk.Entry(ventana,font=("Arial",12),width=30,justify="center")
    Entry(ventana,font=("Arial",12),width=30,justify="center")

    def mostrar_nombre():

        nombre=entrada.get().strip()
        if nobre:
            messagebox.showinfo("Nombre",f"Tu nombre es: {nombre}")
        else:
            messagebox.showwarning("advertencia", "Por favor ingresa tu nombre")

    def borrar_texto():
        entrada.delete(0,tk.END)
    
    marco_botones=tk.Frame(ventana)
    marco_botones.pack(pady=10,expand=True)
    marco_botones.pack(pady=10,anchor="center")

    boton_mostrar=tk.Button(marco_botones,text="Mostrar", font=("Arial",12),bg="green",fg="white",width=10,command=mostrar_nombre)
    boton_mostrar.pack(side=tk.LEFT,padx=10)

    ventana.mainloop()

etiquetas_y_texto()