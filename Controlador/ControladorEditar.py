from tkinter import ttk
from tkinter import *
from Modelo import Producto
from Vista import producto

class ControladorEditar:
    #variable global del modelo
    global mP
    mP = Producto.Producto()
    
    def editarProducto(self, nombre, nombreNuevo, precioNuevo):
        #logica de editar un producto en la BD y luego mostrarlo en la tabla en tiempo real
        fila = mP.editarProducto(nombre, nombreNuevo, precioNuevo)
        if(fila > 0):
            ventana = Tk()
            vP = producto.VentanaProducto(ventana)
            vP.mensaje['text'] = 'Producto Actualizado Correctamente'
        else:
            vP.mensaje['text'] = 'ERROR al actualizar el producto'
        vP.obtenerDatos()
        ventana.destroy()