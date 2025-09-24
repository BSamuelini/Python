nota = float(input("Introduce una nota entre 0 y 10: "))

if nota < 0 or nota > 10:
    print("Nota fuera de rango.")
elif nota <= 5:
    print("Insuficiente")
elif nota <= 6:
    print("Suficiente")
elif nota <= 7:
    print("Bien")
elif nota <= 8:
    print("Notable")
elif nota <= 10:
    print("Sobresaliente")

else:
    print("La nota no es valida")