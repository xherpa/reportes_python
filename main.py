from flask import Flask, jsonify, request
from database.querys import reporte_fibras_hs_is
from pages.AT.home_services import home_services
from pages.AT.Internet_sercice import internet_services
from conversor_horario.conversor_zona_horaria import conversor

app = Flask(__name__)

@app.route('/home_services-internet_services', methods=['POST'])
def generar_reporte():
    # Asegurarse de que la solicitud sea en formato JSON
    if request.is_json:
        # Obtener los datos del cuerpo de la solicitud
        datos = request.get_json()

        # Extraer los campos de los datos
        fecha_inicio = datos.get('date_start')
        fecha_fin = datos.get('date_stop')

        fechas = conversor(fecha_inicio,fecha_fin)

        hs = home_services(fechas[0],fechas[1],fecha_inicio,fecha_fin)
        print(hs)

        if hs == "Datos extraidos con exito":
            is_at = internet_services(fechas[0],fechas[1],fecha_inicio,fecha_fin)
            print(is_at)

            if is_at == "Datos extraidos con exito":
                return jsonify({
                    "message": f"Datos extraidos de Home Services e Internet Services de la fecha {fecha_inicio} hasta {fecha_fin} completado con exito!!"
                }), 200


@app.route('/reporte-fibras-hs-is', methods=['POST'])
def mostrar_reporte():
    # Asegurarse de que la solicitud sea en formato JSON
    if request.is_json:
        # Obtener los datos del cuerpo de la solicitud
        datos = request.get_json()

        # Extraer los campos de los datos
        fecha_inicio = datos.get('date_start')
        fecha_fin = datos.get('date_stop')

        response = reporte_fibras_hs_is(fecha_inicio,fecha_fin)
        return response



if __name__ == '__main__':
    app.run(debug=True)
