a = float(input("ingrese el primer numero:"))
b = float(input("ingrese el segundo numero:"))

proceso = input("ingrese la operacion que desea realizar(suma, resta, multiplicacion, division):")

if proceso == "suma":
    resultado = a + b
    print("El resultado de la suma es:", resultado)
elif proceso == "resta":
    resultado = a - b
    print("El resultado de la resta es:", resultado)
elif proceso == "multiplicacion":
    resultado = a * b
    print("El resultado de la multiplicacion es:", resultado)
elif proceso == "division":
    resultado = a / b
    print("El resultado de la division es:", resultado)
