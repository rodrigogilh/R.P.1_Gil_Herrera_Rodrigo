#Dias, horas, minutos y segundos
s = int(input('Ingrese un numero para convertirlo en tiempo:\n'))
d = s // (24 * 60 * 60)
s = s % (24 * 60 * 60)
h = s // (60 * 60)
s = s % (60 * 60)
m = s // 60
s = s % 60

print(d,'Dias,',h,'Horas,',m,'Minutos,',s,'Segundos')