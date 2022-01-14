import Conexion as conexion

conexion = conexion.connect()
database = conexion[0]
cursor = conexion[1]

class Producto:
    #query que ejecuta la insercion de un producto en la BD
    def registrarProducto(self, nombre, precio):
        query = "INSERT INTO productos VALUES(null, %s, %s)"
        producto = (nombre, precio)
        cursor.execute(query, producto)
        database.commit()
        return cursor.rowcount

    #query que lista los productos de la BD   
    def mostrarProducto(self):
        cursor.execute("SELECT * FROM productos ORDER BY precio_producto")
        lista = []
        lista.append(cursor.rowcount)
        lista.append(cursor.fetchall())
        return lista

    #query que elimina un producto en la BD
    def eliminarProducto(self, nombre):
        cursor.execute("DELETE FROM productos WHERE nombre_producto = " + "'" + nombre + "'")
        database.commit()
        return cursor.rowcount

    #query que edita un producto en la BD
    def editarProducto(self, nombreAntiguo, nombre, precio):
        query = "UPDATE productos SET nombre_producto = %s, precio_producto = %s WHERE nombre_producto = %s"
        producto = (nombre, precio, nombreAntiguo)
        cursor.execute(query, producto)
        database.commit()
        return cursor.rowcount