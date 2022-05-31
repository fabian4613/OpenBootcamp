#Calcular area de un triangulo

import math

altura = int(input("Cual es la altura del triangulo? (En metros) "))
base = int(input("y la base? "))

def triangulo(altura,base):

    operacion1 = (altura+base)/2
    return round(operacion1)

#A partir de aqui, uso math
print('El area del triangulo es:',(triangulo(altura,base)))

print("Cual es el radio del circulo?")
r = float(input())
a = math.pi * (r * r)
print("El area del circulo con radio de",r, "es:",round(a, 2))
