from tkinter import ttk
from tkinter import *
from Vista import producto
from Modelo import Producto
from Vista import editar

class ControladorProducto:
    #ventana
    ventana = Tk()
    #variable global de la vista del producto
    global vP
    vP = producto.VentanaProducto(ventana)
    #variable global del modelo del producto
    global mP
    mP = Producto.Producto()

    def __init__(self, ventana):       
        #boton agregar producto
        ttk.Button(vP.contenedor, text='Insertar Producto', command = self.agregarProducto).grid(
            row = 3,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky = W + E
        )

        #boton eliminar producto
        ttk.Button(vP.contenedor, text = 'Eliminar Producto', command = self.eliminarProducto).grid(
            row = 5,
            column = 1,
        )

        #boton editar producto
        ttk.Button(vP.contenedor, text = 'Editar Producto', command = self.modificarProducto).grid(
            row = 5,
            column = 0,
            padx = 12,
            pady = 12,
            sticky = W + E
        )
        vP.obtenerDatos()

    #funcion que valida que los datos no vengan vacios
    def validar(self):
        if(len(vP.nombre.get()) > 0 and len(vP.precio.get()) > 0):
            return True
        else:
            return False

    #logica para agregar un producto en la BD y actualizar los datos en tiempo real
    def agregarProducto(self):
        if(self.validar()):
            nombre = vP.nombre.get()
            precio = int(vP.precio.get())
            fila = mP.registrarProducto(nombre, precio)
            if(fila > 0):
                vP.mensaje['text'] = f'{nombre} insertado correctamente'
                vP.nombre.delete(0, END)
                vP.precio.delete(0, END)
            else:
                vP.mensaje['text'] = "ERROR al insertar el producto"
                nombre.delete(0, END)
                precio.delete(0, END)
        else:
             vP.mensaje['text'] = "ERROR no ha ingresado datos"
        vP.obtenerDatos()

    #logica para eliminar un producto de la BD y actualizar los datos en tiempo real
    def eliminarProducto(self):
        try:
            nombre = vP.tabla.item(vP.tabla.selection())['text']
            fila = mP.eliminarProducto(nombre)
            if(fila > 0):
                vP.mensaje['text'] = f'{nombre} eliminado correctamente'
            else:
                vP.mensaje['text'] = 'ERROR debe seleccionar un producto'
            vP.obtenerDatos()
        except:
            vP.mensaje['text'] = 'ERROR al eliminar el producto'

    #funcion que abre la ventana editar
    def modificarProducto(self):
        nombre = vP.tabla.item(vP.tabla.selection())['text']
        precio = vP.tabla.item(vP.tabla.selection())['values']
        vE = editar.VentanaModificar(self.ventana, nombre, precio)