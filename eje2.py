#Cree un programa que tome el radio de un círculo e imprima su área y perímetro.
import math
radio = float(input("Ingrese el radio del círculo: "))

area_circulo = math.pi * radio**2

perimetro_circulo = 2 * math.pi * radio

print("El área del círculo es: {area_circulo:.2f}")
print("El perímetro del círculo es: {perimetro_circulo:.2f}")