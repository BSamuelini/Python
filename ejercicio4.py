# Crea un programa llamado Media.py que le pida al usuario 4 números enteros y calcule su media (real). 
# La media debe mostrarse en pantalla con 3 cifras decimales.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))

media = (num1 + num2 + num3 + num4) / 4

print("La media es: {:.3f}".format(media))