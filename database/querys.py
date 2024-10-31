import json
from .database_conexion import connect_to_mysql, close_connection
from pg import Error

db = connect_to_mysql()


def extraccion_ids_hs(date_start, date_stop):
    def execute_query(connection):
        try:
            data = []
            cursor = connection.cursor()
            query = f"SELECT paginas_negocio.nombre_negocio,facebook_data.ad_id, facebook_data.ad_name, facebook_data.result, facebook_data.cost_per_result, facebook_data.reach, facebook_data.impressions, facebook_data.spend, facebook_data.cpm,facebook_data.ctr, facebook_data.frecuency, facebook_data.cost_per_unique_click, facebook_data.objetive, facebook_data.date_start, facebook_data.date_stop FROM facebook_data INNER JOIN paginas_negocio WHERE paginas_negocio.id = facebook_data.id_business_page and (paginas_negocio.nombre_negocio= 'Home Services') and (facebook_data.date_start = '{date_start}' AND facebook_data.date_stop = '{date_stop}');"
            cursor.execute(query)

            # Obtener los resultados de la consulta
            resultados = cursor.fetchall()
            for fila in resultados:
                data.append(fila)

            return data

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    if db :
        data = execute_query(db)
        
        # close_connection(db)
        return data



def extraccion_ids_is(date_start, date_stop):
    def execute_query(connection):
        try:
            data = []
            cursor = connection.cursor()
            query = f"""
                        SELECT paginas_negocio.nombre_negocio,facebook_data.ad_id, facebook_data.ad_name, facebook_data.result, facebook_data.cost_per_result, facebook_data.reach, 
                        facebook_data.impressions, facebook_data.spend, facebook_data.cpm,facebook_data.ctr, facebook_data.frecuency, facebook_data.cost_per_unique_click, 
                        facebook_data.objetive, facebook_data.date_start, facebook_data.date_stop 
                        FROM facebook_data 
                        INNER JOIN paginas_negocio 
                        WHERE paginas_negocio.id = facebook_data.id_business_page 
                        AND (paginas_negocio.nombre_negocio= 'AT&T Dealer') 
                        AND (facebook_data.date_start = '{date_start}' 
                        AND facebook_data.date_stop = '{date_stop}');
            """
            cursor.execute(query)

            # Obtener los resultados de la consulta
            resultados = cursor.fetchall()
            for fila in resultados:
                data.append(fila)

            return data

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    if db :
        data = execute_query(db)
        
        # close_connection(db)
        return data
        

def extraccion_ids_frontier(date_start, date_stop):
    def execute_query(connection):
        try:
            data = []
            cursor = connection.cursor()
            query = f"""
                        SELECT paginas_negocio.nombre_negocio,facebook_data.ad_id, facebook_data.ad_name, facebook_data.result, facebook_data.cost_per_result, facebook_data.reach, 
                        facebook_data.impressions, facebook_data.spend, facebook_data.cpm,facebook_data.ctr, facebook_data.frecuency, facebook_data.cost_per_unique_click, 
                        facebook_data.objetive, facebook_data.date_start, facebook_data.date_stop 
                        FROM facebook_data 
                        INNER JOIN paginas_negocio 
                        WHERE paginas_negocio.id = facebook_data.id_business_page 
                        AND (paginas_negocio.nombre_negocio= 'Frontier Services') 
                        AND (facebook_data.date_start = '{date_start}'
                        AND facebook_data.date_stop = '{date_stop}');
                        """
            cursor.execute(query)
            resultados = cursor.fetchall()
            for fila in resultados:
                data.append(fila)

            return data

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    if db :
        data = execute_query(db)

        return data


def insert_datos(tipo, total, pagina, ad_id, date_start, date_stop):
    def insert_data(connection):
        try:
            cursor = connection.cursor()
            query = """INSERT INTO hubspot (pagina, tipo, total, fk_ad_id, date_start, date_stop) VALUES (%s, %s, %s, %s, %s, %s)"""
            data = (pagina,tipo,total,ad_id, date_start, date_stop)
            cursor.execute(query,data)

            connection.commit()
            print("Datos insertados correctamente")


        except Error as e:
            print(f"Error al insertar datos: {e}")

    if db :
        insert_data(db)
        # close_connection(db)


def reporte_fibras_hs_is(date_start, date_stop):
    def execute_query(connection):
        try:
            cursor = connection.cursor()
            query = f"""
                        SELECT facebook_data.ad_id, facebook_data.ad_name, facebook_data.result, facebook_data.cost_per_result, facebook_data.reach, 
                        facebook_data.impressions,facebook_data.spend,facebook_data.cpm,facebook_data.cpp,facebook_data.ctr,facebook_data.frecuency,
                        facebook_data.cost_per_unique_click,facebook_data.objetive, fibra.total as 'total_Fibra', dsl.total as 'total_dsl', sales_fibra.total as 'total_sales_fibra', 
                        sales_dsl.total as 'total_sales_dsl',  credit_checks.total as 'total_credit_check', sales_others_companies.total as 'total_other_companies'
                        FROM facebook_data
                        INNER JOIN (SELECT * FROM hubspot WHERE hubspot.tipo = "dsl" AND 
                        (hubspot.date_start = "{date_start}" AND hubspot.date_stop = "{date_stop}")) as dsl on facebook_data.ad_id = dsl.fk_ad_id
                        INNER JOIN (SELECT * FROM hubspot WHERE hubspot.tipo = "fibra" AND 
                        (hubspot.date_start = "{date_start}" AND hubspot.date_stop = "{date_stop}")) as fibra on facebook_data.ad_id = fibra.fk_ad_id
                        INNER JOIN (SELECT * FROM hubspot WHERE hubspot.tipo = "sales_dsl" AND 
                        (hubspot.date_start = "{date_start}" AND hubspot.date_stop = "{date_stop}")) as sales_dsl on facebook_data.ad_id = sales_dsl.fk_ad_id
                        INNER JOIN (SELECT * FROM hubspot WHERE hubspot.tipo = "sales_fibra" AND 
                        (hubspot.date_start = "{date_start}" AND hubspot.date_stop = "{date_stop}")) as sales_fibra on facebook_data.ad_id = sales_fibra.fk_ad_id
                        INNER JOIN (SELECT * FROM hubspot WHERE hubspot.tipo = "credit_checks" AND 
                        (hubspot.date_start = "{date_start}" AND hubspot.date_stop = "{date_stop}")) as credit_checks on facebook_data.ad_id = credit_checks.fk_ad_id
                        INNER JOIN (SELECT * FROM hubspot WHERE hubspot.tipo = "sales_others_companies" AND 
                        (hubspot.date_start = "{date_start}" AND hubspot.date_stop = "{date_stop}")) as sales_others_companies on facebook_data.ad_id = sales_others_companies.fk_ad_id
                        WHERE facebook_data.date_start = "{date_start}" AND facebook_data.date_stop = "{date_stop}";
                        """
            cursor.execute(query)

            # Obtener los nombres de las columnas
            columnas = [columna[0] for columna in cursor.description]

            # Obtener los resultados de la consulta
            resultados = cursor.fetchall()

            # Convertir los resultados en una lista de diccionarios
            datos_json = [dict(zip(columnas, fila)) for fila in resultados]

            print(json.dumps(datos_json, indent=4))

            return json.dumps(datos_json, indent=4)

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    if db :
        data = execute_query(db)
        
        close_connection(db)
        return data
