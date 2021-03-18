#Triangulos
l1 = int(input('Ingrese la primera longitud:\n'))
l2 = int(input('Ingrese la segunda longitud:\n'))
l3 = int(input('Ingrese la tercera longitud:\n'))

if l1 == l2 == l3:
    print('Es un triangulo equilatero.')
else:
    if l3!= l1 == l2 or l2!= l3== l1 or l1!= l2==l3:
        print('Es un triangulo isoceles.')
    else:
        print('Es un triangulo escaleno.')
        