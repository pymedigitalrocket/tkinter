import mysql.connector

def connect():
    database = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "proyecto_tkinter"
    )
    cursor = database.cursor(buffered=True)
    return [database, cursor]