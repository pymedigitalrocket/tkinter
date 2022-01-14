from tkinter import ttk
from tkinter import *
from Controlador import ControladorProducto as cP

#main
if __name__ == '__main__':
    ventana = Tk()
    ventana.destroy()
    #iniciar la clase de la ventana producto
    aplicacion = cP.ControladorProducto(ventana)
    #arrancar la ventana
    ventana.mainloop()