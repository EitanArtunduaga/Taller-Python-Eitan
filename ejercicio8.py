nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))

nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 71:
    print("Hola", nombre, "tu edad es", edad, "y tu promedio es", promedio, " has aprobado")
else:
    print("Hola", nombre, "tu edad es", edad, "y tu promedio es", promedio, " has reprobado")