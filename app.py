from flask import Flask, request, jsonify
from scripts.time_api import convert_date_calendar, montu_time_to_dict
import os 

app = Flask(__name__)

@app.route('/convert_date', methods=['GET'])
def api_convert_date():
    """Endpoint de Flask para convertir fechas."""
    # Extraer parámetros de la solicitud
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    hour = request.args.get('hour')
    min = request.args.get('min')
    sec = request.args.get('sec')
    calendar = request.args.get('calendar')

    # Validar que todos los parámetros están presentes
    if not all([year, month, day, hour, min, sec, calendar]):
        return jsonify({"error": "Todos los parámetros son necesarios"}), 400

    # Lógica de la función
    try:
        mtime = convert_date_calendar(year, month, day, hour, min, sec, calendar)
        result_dict = montu_time_to_dict(mtime)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Crear y devolver la respuesta JSON
    return jsonify(result_dict)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
