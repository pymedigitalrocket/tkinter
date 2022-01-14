from tkinter import ttk
from tkinter import *
from Controlador import ControladorEditar

class VentanaModificar:
    global cE
    cE = ControladorEditar.ControladorEditar()
    def __init__(self, ventana, nombre, precio):
        #ventana editar producto
        self.ventana = Tk()
        self.ventana.title("Modificar Producto")
        self.ventana.geometry("300x150")
        self.ventana.resizable(0,0)
        self.nombre = nombre

        #formulario con los antiguos valores del producto
        self.contenedor = LabelFrame(self.ventana, text="Modificar Datos del Producto")
        self.contenedor.grid(
            row = 0,
            column = 0,
            columnspan = 3,
            padx = 20,
            pady = 20
        )

        #label nombre actual
        Label(self.contenedor, text="Nombre: ").grid(
            row = 1,
            column = 0
        )

        #input nombre actual
        self.nombreAntiguo = Entry(self.contenedor, textvariable = StringVar(self.contenedor, nombre))
        self.nombreAntiguo.focus()
        self.nombreAntiguo.grid(
            row = 1,
            column = 1,
            padx = 5
        )

        #label precio actual
        Label(self.contenedor, text='Precio:').grid(
            row = 2,
            column = 0
        )

        #input precio actual
        self.precioAntiguo = Entry(self.contenedor, textvariable = StringVar(self.contenedor, precio))
        self.precioAntiguo.grid(
            row = 2,
            column = 1
        )

        #boton de editar producto que se vera en la vista editar
        ttk.Button(self.contenedor, text = 'Editar Producto', command = self.vEditarProducto).grid(
            row = 5,
            column = 0,
            padx = 12,
            pady = 12,
            sticky = W + E
        )

    #funcion que comunica la vista editar con el controlador editar
    def vEditarProducto(self):
        nombreNuevo = self.nombreAntiguo.get()
        precioNuevo = int(self.precioAntiguo.get())
        cE.editarProducto(self.nombre, nombreNuevo, precioNuevo)
        self.ventana.destroy()