import datetime
year=2017
mes = 1
dia = 12

try:
    fecha = datetime.date(year,mes,dia)
    print (fecha.weekday() )

except ValueError:
    print("Hubo un error en la fecha")
