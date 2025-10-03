nums = [6, 3, 7, 2, 9, 4, 6, 6, 1, 3, 2, 8, 5]

#Suma de todos
suma = sum(nums)
print("1) Suma de todos los números:", suma)

#Máximo
maximo = max(nums)
print("2) Número máximo:", maximo)

#Ocurrencias
ocurrencias = nums.count(6)
print("3) Ocurrencias del número 6:", ocurrencias)

#Media sin sum
contador = 0
x = []
for n in nums:
    if n == x:
        contador += 1
print("4) El número", x, "aparece", contador, "veces.")

#Lista con pares
pares = []
for n in nums:
    if n % 2 == 0:
        pares.append(n)
print("5) Números pares:", pares)

#Máx(nums) - min(nums)
maximo =nums[0]
minimo = nums[0]

for n in nums:
    if n > maximo:
        maximo = n
    if n < minimo:
        minimo = n

print("6) Diferencia entre máximo y mínimo:", maximo - minimo)

#Buscar el primer indice de un número
x = int(input("7) Número a buscar: "))
indice = -1
for i in range(len(nums)):
    if nums[i] == x:
        indice = i
        break

print("Índice:", indice)
