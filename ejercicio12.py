numeros = str(input("Introduce unos números separados por espacios: "))

partes = numeros.split()

print("La suma de los números es:", sum(map(int, partes)))