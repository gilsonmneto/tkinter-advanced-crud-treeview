"""CRUD with Tkinter"""
import tkinter as tk
from tkinter import ttk


class MainApplication:
    """Create UserInterface"""
    def __init__(self, window):
        self.window = window
        self.window.title('Movie CRUD')

        # crear un contenedor frame
        self.frame = tk.Frame(self.window)
        self.frame.grid(row=0, column=0, columnspan=6, pady=20)

        # entrada de nombre
        self.name_label = tk.Label(self.frame, width= 60, text='Nombre: ').grid(row=1, column=0)
        self.name_entry = tk.Entry(self.frame).grid(row=2, column=1)

        # entrada de telefono
        tk.Label(self.frame, text='Telefono: ').grid(row=2, column=0)
        self.telefono = tk.Entry(self.frame).grid(row=2, column=1)

        # entrada de ciudad
        tk.Label(self.frame, text='Ciudad: ').grid(row=3, column=0)
        self.ciudad = tk.Entry(self.frame).grid(row=3, column=1)

        # entrada de email
        tk.Label(self.frame, text='Email: ').grid(row=4, column=0)
        self.email = tk.Entry(self.frame).grid(row=4, column=1)

        # Boton para añadir
        tk.Button(self.frame, text='Guardar contacto', command="").grid(row=5, columnspan=2, sticky=tk.W + tk.E)

        # Salida de mensajes
        self.mensaje = tk.Label(text='', fg='red')
        self.mensaje.grid(row=3, column=0, columnspan=2, sticky=tk.W + tk.E)

        # Crear tabla
        self.tree = ttk.Treeview(height=20, columns=("Nombre", "Telefono", "Ciudad",))
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=tk.CENTER)
        self.tree.heading('#1', text='Telefono', anchor=tk.CENTER)
        self.tree.heading('#2', text='Ciudad', anchor=tk.CENTER)
        self.tree.heading('#3', text='Email', anchor=tk.CENTER)

        # Botones
        tk.Button(text='Eliminar', command="").grid(row=6, column=0, sticky=tk.W + tk.E)
        tk.Button(text='Editar', command="").grid(row=6, column=1, sticky=tk.W + tk.E)


def main():
    """Create Main Window"""
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    main()
