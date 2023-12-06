# Cree un programa que tome el precio de un producto e imprima su precio final al consumidor con un IVA de 19%.
precio_producto = float(input("Ingrese el precio del producto: "))

iva_porcentaje = 19
precio_final = precio_producto * (1 + iva_porcentaje / 100)

print("El precio final al consumidor con un IVA del {iva_porcentaje}% es: {precio_final:.2f}")
