import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")


def connect_to_mysql():
    try:
        # Crear la conexión
        connection = mysql.connector.connect(
            host=HOST,  # o la IP del servidor donde está tu base de datos
            user=USER,
            password=PASSWORD,
            database=DATABASE,
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            return connection

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None


def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión cerrada")
