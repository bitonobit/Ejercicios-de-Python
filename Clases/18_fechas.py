import datetime
# La fecha contiene año, mes, día, hora, minuto, segundo y microsegundo.
x = datetime.datetime.now()
print(x)                    # Devuelve 2024-05-01 20:31:43.319693
print(x.year)               # Devuelve el año 2024
print(x.strftime("%A"))     # Devuelve Wednesday
x = datetime.datetime(1973, 4, 2)   #Crear una fecha
print(x)
x = datetime.datetime(2004, 1, 22)
print(x.strftime("%B"))     # Devuelve January

# *************************************************
#               Formatos
# *************************************************
# Código       Descripción
# %a            Mon
# %A            Monday
# %w	        Día de la semana 0-6, 0 es Sunday	
# %d	        Día del mes 01-31		
# %b	        Jan
# %B	        January	
# %m	        Mes como número 01-12	
# %y	        Año 2 dígitos 24	
# %Y	        2024	
# %H	        Hora 00-23	 	
# %I	        Hora 00-12	 	
# %p	        AM/PM	 
# %M	        Minutos 00-59	 
# %S	        Segundos 00-59	
# %f	        Microsegundos 000000-999999	548513	
# %z	        UTC offset	+0100	
# %Z	        Timezone	CST	
# %j	        Día del año 001-366	365	
# %U	        Semana del año, 00-53 comienzan en domingo		
# %W	        Semana del año, 00-53 comienzan en lunes
# %c	        Mon Dec 31 17:41:00 2018	
# %C	        Century	20	
# %x	        12/31/18	
# %X	        17:41:00	
# %G	        ISO 8601 año	2024	
# %u	        ISO 8601 día de la semana (1-7)	 
# %V	        ISO 8601 Núm de semana (01-53) 