from pg import DB, Error
from config.config import HOST,USER,PASSWORD,DATABASE,PORT

def connect_to_mysql():
    try:
        # Crear la conexión
        connection = DB(dbname=DATABASE,host=HOST,port=PORT, user=USER, passwd=PASSWORD)
        print(connection)
        print("Conexión exitosa a la base de datos MySQL")
        return connection

    except Error as e:
        print(f"Error al conectar a la base de datos : {e}")
        return None

def close_connection(connection):
    connection.close()
    print("Conexion cerrada")
