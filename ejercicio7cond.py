temperatura = int(input("ingresa la temperatura: "))

if temperatura <= 20:
    print("Hace frío")
elif temperatura > 20 and temperatura < 30:
    print("temperatura agradable")
else:
    print("Hace calor")