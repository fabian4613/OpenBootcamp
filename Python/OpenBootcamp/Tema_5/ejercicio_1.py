#Calcular area de un triangulo

import math

altura = int(input("Cual es la altura del triangulo? (En metros) "))
base = int(input("y la base? "))

def triangulo(altura,base):

    operacion1 = (altura+base)/2
    return round(operacion1)


print(f'El area del triangulo es:',(triangulo(altura,base)))

#A partir de aqui, uso math

def area_circulo(radio: float) -> float:
    return (math.pi*(radio**2))

print(f"Área del círculo: {area_circulo(4)}")
