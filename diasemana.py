from datetime import datetime
def obtener_dia_semana(fecha_evento):

    dia_semana = fecha_evento.strftime("%A")

    return dia_semana

fecha_atentado = datetime(2001, 9, 11)
print(obtener_dia_semana(fecha_atentado))