#Cree un programa que lea una cantidad e imprima un porcentaje a calcular requerido sobre esa cantidad.
cantidad = float(input("Ingrese la cantidad: "))

porcentaje = float(input("Ingrese el porcentaje a calcular: "))

resultado = cantidad * (porcentaje / 100)

print("El {porcentaje}% de {cantidad} es: {resultado:.2f}")
