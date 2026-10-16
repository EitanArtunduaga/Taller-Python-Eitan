edad = int(input("¿Cuál es tu edad? "))
permiso = input("¿permiso de tus padres?(true/false): ")

if edad >= 18 and permiso:
    print("puedes participar")
else:
    print("no puedes participar")