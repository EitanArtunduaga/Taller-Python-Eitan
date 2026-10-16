precio = int(input("ingresa el precio del producto: "))

if precio >= 100:
    precio_final = precio - (precio / 10)
else:
    precio_final = precio   

print("Su descuento es de", precio - precio_final, "$", "y el precio final es: ", precio_final ,"$")