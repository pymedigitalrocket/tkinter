use proyecto_tkinter;

CREATE TABLE productos(
    id_producto INT AUTO_INCREMENT NOT NULL,
    nombre_producto VARCHAR(50) NOT NULL,
    preccio_producto int(7) NOT NULL,
    CONSTRAINT pk_producto PRIMARY KEY(id_producto)
)ENGINE=InnoDb;