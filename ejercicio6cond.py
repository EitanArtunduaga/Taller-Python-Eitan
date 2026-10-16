nota = int(input("ingresa tu nota: "))

if nota >= 91:
    print("Excelente")
elif nota >= 71 and nota <= 90:
    print("Aprobaste")
else:
    print("Reprobaste")