from tkinter import ttk
from tkinter import *
from Modelo import Producto

#clase ventana producto
class VentanaProducto:
    def __init__(self, ventana):
        global mP
        mP = Producto.Producto()
        self.ventana = ventana
        self.ventana.title("Ventana Productos")
        self.ventana.geometry("500x500")
        self.ventana.resizable(0,0)

        #contenedor
        self.contenedor = LabelFrame(self.ventana, text='Ingresar Nuevo Producto')
        self.contenedor.grid(
            row = 0,
            column = 0,
            columnspan = 3,
            padx = 20,
            pady = 20
        )
        #label nombre
        Label(self.contenedor, text='Nombre:').grid(
            row = 1,
            column = 0
        )
        #input nombre
        self.nombre = Entry(self.contenedor)
        self.nombre.focus()
        self.nombre.grid(
            row = 1,
            column = 1,
            padx = 5
        )
        #label precio
        Label(self.contenedor, text='Precio:').grid(
            row = 2,
            column = 0
        )
        #input precio
        self.precio = Entry(self.contenedor)
        self.precio.grid(
            row = 2,
            column = 1
        )
        
        #mensaje de salida
        self.mensaje = Label(
            text = '',
            fg = 'red'
        )
        self.mensaje.grid(
            row = 3,
            column = 0,
            columnspan = 2,
            sticky = W + E
        )

        #tablas
        self.tabla = ttk.Treeview(height = 10, column = 2)
        self.tabla.grid(row = 4, column = 0, columnspan = 2, padx = 50)
        self.tabla.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tabla.heading('#1', text = 'Precio', anchor = CENTER)

    def obtenerDatos(self):
        #mostrar los datos del producto en la tabla de la vista producto
        self.limpiarTabla()
        mostrar = mP.mostrarProducto()
        for producto in mostrar[1]:
            if(mostrar[0] > 0):
                self.tabla.insert('', 0, text = producto[1], values = producto[2])

    def limpiarTabla(self):
        #limpiar datos en la tabla
        registros = self.tabla.get_children()
        for dato in registros:
            self.tabla.delete(dato)