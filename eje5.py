#Cree un programa que tome el valor de un producto e imprima su precio final si éste tiene siempre un descuento del 10%.
valor_producto = float(input("Ingrese el valor del producto: "))

descuento_porcentaje = 10
descuento = valor_producto * (descuento_porcentaje / 100)

precio_final = valor_producto - descuento

print("El precio final con un descuento del {descuento_porcentaje}% es: {precio_final:.2f}")
