nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))

mayores = sum(n > 4 for n in [nota1, nota2, nota3])

if mayores == 0:
    nota_final = 0
elif mayores < 3:
    nota_final = 2
else:
    nota_final = 0.3 * nota1 + 0.2 * nota2 + 0.5 * nota3

print("La nota final es:", nota_final)