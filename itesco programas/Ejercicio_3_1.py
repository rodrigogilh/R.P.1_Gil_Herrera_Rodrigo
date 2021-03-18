# A,B,C
A = int(input('¿Cuantas ventas tiene el producto A? '))
B = int(input('¿Cuantas ventas tiene el producto B? '))
C = int(input('¿Cuantas ventas tiene el producto C? '))

#Mayor
if A > B and A > C:
    print('a) Las ventas del producto A son las más elevadas')
if B > A and B > C:
    print('a) Las ventas del producto B son las más elevadas')
if C > A and C > B:
    print('a) Las ventas del producto C son las más elevadas')

#Menor
if A < B and A < C:
    print('b) Ningún producto tiene unas ventas inferiores a',A)
if B < A and B < C:
    print('b) Ningún producto tiene unas ventas inferiores a',B)
if C < A and C < B:
    print('b) Ningún producto tiene unas ventas inferiores a',C)

#Mitad
if A < B and A < C:
    if B < C:
        print('c) Algún producto tiene unas ventas superiores a',B)
if B < A and B < C:
    if A < C:
        print('c) Algún producto tiene unas ventas superiores a',A)
if C < B and C < A:
    if C < B:
        print('c) Algún producto tiene unas ventas superiores a',C)

#Media
m = int(A + B + C)/3
print('d) La media de ventas es superior a:',m)

#Menor2
if A < B and A < C:
     print('e) El producto A no es el más vendido.')
if B < A and B < C:
    print('e) El producto B no es el más vendido.')
if C < A and C < B:
     print('e) El producto C no es el más vendido.')

#
s = int(A + B + C)
s1 = int(s/2)
s2 = int(s+s1)
print('f) El total de ventas esta entre',s1,'y',s2)

