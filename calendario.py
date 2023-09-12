import datetime
import calendar

fecha_actual = datetime.datetime.now()

print(calendar.month(fecha_actual.year, fecha_actual.month))