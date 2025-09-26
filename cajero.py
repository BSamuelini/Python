saldo = 1000

print("El saldo es igual a:", saldo)

while saldo > 0:
    opcion = input("¿Desea sacar dinero? (s/n): ").lower()
    if opcion != 's':
        print("Gracias por usar el cajero. Su saldo final es:", saldo)
        break

    retiro = int(input("Ingrese la cantidad a retirar: "))

    if retiro > saldo:
        print("No tiene suficiente saldo")
    else:
        saldo -= retiro
        print("Retiro exitoso. Su nuevo saldo es:", saldo)