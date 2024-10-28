from datetime import datetime
import pytz

# Definir la zona horaria de Colombia
zona_horaria_colombia = pytz.timezone('America/Bogota')  # Hora estándar de Colombia (UTC-5)

def conversor (date_start, date_stop):
    dates = []
    # Función que convierte de hora colombiana a UTC
    def convertir_hora_colombiana_a_utc(fecha_hora_str):
        # Convertir la cadena de fecha y hora a un objeto datetime
        fecha_hora = datetime.strptime(fecha_hora_str, '%Y-%m-%dT%H:%M:%S')

        # Localizar la fecha y hora en la zona horaria de Colombia
        fecha_hora_colombia = zona_horaria_colombia.localize(fecha_hora)

        # Convertir la fecha y hora a UTC
        fecha_hora_utc = fecha_hora_colombia.astimezone(pytz.utc)

        return fecha_hora_utc.strftime('%Y-%m-%dT%H:%M:%S')

    # Ejemplos de uso
    fecha_inicio_colombia = f'{date_start}T00:00:00'  # Fecha en hora de Colombia
    fecha_fin_colombia = f'{date_stop}T23:59:59'     # Fecha en hora de Colombia

    # Convertir a UTC
    fecha_inicio_utc = convertir_hora_colombiana_a_utc(fecha_inicio_colombia)
    dates.append(fecha_inicio_utc)
    fecha_fin_utc = convertir_hora_colombiana_a_utc(fecha_fin_colombia)
    dates.append(fecha_fin_utc)

    # Imprimir los resultados
    # print("Fecha Inicio (Colombia) convertida a UTC:", fecha_inicio_utc)
    # print("Fecha Fin (Colombia) convertida a UTC:", fecha_fin_utc)

    # print(dates)
    return dates
