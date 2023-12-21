import montu

# Función pára llevar la estructura de objeto de tiome en montu a un json
def montu_time_to_dict(mtime):
    """
    Convierte un objeto Montu Time a un diccionario para facilitar la serialización JSON.

    Args:
    mtime (Montu Time Object): Objeto Montu Time a convertir.

    Returns:
    dict: Diccionario representando el objeto Montu Time.
    """
    return {
        "time_as_strings": {
            "spice": mtime.readable.datespice,  # Date in gregorian proleptic
            "proleptic": mtime.readable.datepro,  # Date in gregorian proleptic
            "mixed": mtime.readable.datemix,  # Date in mixed
            "caniucular": mtime.readable.datecan  # Date in caniucular (civil egyptian)
        },
        "time_in_uniform_scales": {
            "deltat": mtime.deltat,  # Delta T
            "tt": mtime.tt,  # Date in ephemerides time (tt scale)
            "et": mtime.et,  # Date in ephemerides time (utc scale)
            "jd_utc": mtime.jed  # Date in Julian Day (utc scale)
        }
    }

def convert_date_calendar(year, month, day, hour, min, sec, calendar):
    """
    Convierte una fecha y hora a un formato de calendario específico.

    Args:
    year (int): Año de la fecha.
    month (int): Mes de la fecha.
    day (int): Día de la fecha.
    hour (int): Hora del día.
    min (int): Minutos de la hora.
    sec (int): Segundos de los minutos.
    calendar (str): Tipo de calendario a usar.

    Returns:
    Montu Time Object: Objeto Montu Time representando la fecha en el calendario especificado.
    """
    date = f'{int(year or 1)}-{int(month or 1):02d}-{int(day or 1):02d} {int(hour or 0):02d}:{int(min or 0):02d}:{int(sec or 0):02d}'
    mtime = montu.Time(date, format='iso', scale='utc', calendar=calendar)
    return mtime

#print(convert_date_calendar(2002,7,26,9,32,0,'caniucular'))