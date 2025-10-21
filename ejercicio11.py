n = int(input("Dime cuántos números vas a introducir: "))

if n <= 0:
    print("Debes introducir un número mayor que 0.")
else:
    print(f"Escribe {n} números:")

numeros = []

for i in range(n):
    num = int(input())
    while num <= 0:
        print("Por favor, introduce un número positivo:")
        num = int(input())
    numeros.append(num)

mayor = max(numeros)
menor = min(numeros)

print(f"El mayor es {mayor}")
print(f"El menor es {menor}")