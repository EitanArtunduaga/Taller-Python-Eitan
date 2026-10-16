edad = int(input("¿Cuál es tu edad? "))
entrada = input("¿tienes entradas para el evento?(true/false): ")

if edad >= 16 and entrada:
    print("puedes participar")  
else:
    print("no puedes participar")