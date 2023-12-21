import functions_framework
from scripts.time_api import convert_date_calendar, montu_time_to_dict

@functions_framework.http
def api_convert_date(request):
    """HTTP Cloud Function para convertir fechas."""
    # Extraer parámetros de la solicitud
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    hour = request.args.get('hour')
    min = request.args.get('min')
    sec = request.args.get('sec')
    calendar = request.args.get('calendar')

    # Lógica de la función
    mtime = convert_date_calendar(year, month, day, hour, min, sec, calendar)
    result_dict = montu_time_to_dict(mtime)

    # Crear y devolver la respuesta JSON
    return result_dict  # Flask jsonify no es necesario; Google Cloud Functions maneja la conversión a JSON
