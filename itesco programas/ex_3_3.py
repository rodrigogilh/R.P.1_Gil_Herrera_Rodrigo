#Humano - perro
def edad_prro(ep):
    if ep < 2:
        return ep*10.5
    else:
        return 21 + (ep-2)*4
ep = int(input('Ingrese su edad:\n'))
if ep > 0:
    t = edad_prro(ep)
    print('La edad en años perro serian:',t,'años')