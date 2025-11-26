import tkinter as tk
from tkinter import messagebox
from directorio import inicializar_csv, guardar_persona


ventana = None
entrada_nombre = None
entrada_numero = None
etiqueta_estado = None

def agregar_persona():
    nombre = entrada_nombre.get().strip()
    numero = entrada_numero.get().strip()

    if not nombre or not numero:
        messagebox.showwarning("Error", "Debes llenar ambos campos")
        return

    if guardar_persona(nombre, numero):
        etiqueta_estado.config(text=f"Agregado: {nombre}")
        entrada_nombre.delete(0, tk.END)
        entrada_numero.delete(0, tk.END)
        entrada_nombre.focus()
        ventana.after(5000, lambda: etiqueta_estado.config(text=""))
    else:
        messagebox.showerror("Error", "No se pudo guardar")

def limpiar_campos():
    entrada_nombre.delete(0, tk.END)
    entrada_numero.delete(0, tk.END)
    etiqueta_estado.config(text="")
    entrada_nombre.focus()


def construir_interfaz():
    global ventana, entrada_nombre, entrada_numero, etiqueta_estado
    ventana = tk.Tk()
    ventana.title("Directorio")

    etiqueta_nombre = tk.Label(ventana,text="Nombre:")
    etiqueta_nombre.pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()

    etiqueta_numero = tk.Label(ventana, text="Numero:")
    etiqueta_numero.pack()
    entrada_numero = tk.Entry(ventana)
    entrada_numero.pack()

    boton_agregar = tk.Button(ventana, text="Agregar persona",command=agregar_persona)
    boton_agregar.pack()

    boton_limpiar = tk.Button(ventana, text="Limpiar campos",command=limpiar_campos)
    boton_limpiar.pack()

    etiqueta_estado = tk.Label(ventana, text="")
    etiqueta_estado.pack()

    entrada_nombre.focus_set()


def main():
    inicializar_csv()
    construir_interfaz()
    ventana.mainloop()


if __name__ == "__main__":
    main()