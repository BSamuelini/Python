import random

numero = random.randint(1, 10)

adivinar = int(input("Adivina el número entre 1 y 10: "))

while adivinar != numero:
    if adivinar < numero:
        print("Demasiado bajo")
    else:
        print("Demasiado alto")
    adivinar = int(input("Adivina el número entre 1 y 10: "))

print("¡Felicidades! Has adivinado el número.")