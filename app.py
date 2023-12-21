from scripts.time_api import convert_date_calendar, montu_time_to_dict
from flask import Flask, request, jsonify
from flask_cors import CORS

# Crear la instancia de la aplicación Flask
app = Flask(_name_)

# Configurar CORS para permitir todas las fuentes
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/convert_date', methods=['GET'])
def api_convert_date():
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    hour = request.args.get('hour')
    min = request.args.get('min')
    sec = request.args.get('sec')
    calendar = request.args.get('calendar')

    mtime = convert_date_calendar(year, month, day, hour, min, sec, calendar)
    result_dict = montu_time_to_dict(mtime)
    return jsonify(result_dict)

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=8080)