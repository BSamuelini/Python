def main():
    lista = []
    print("Introduce números (0 para terminar).")
    while True:
        try:
            n = int(input("Número: "))
        except ValueError:
            print("Entrada no válida. Introduce un entero.")
            continue
        if n == 0:
            break
        lista.append(n)

    if not lista:
        print("No se introdujeron números.")
        return

    while True:
        try:
            objetivo = int(input("¿Qué número quieres buscar?: "))
            break
        except ValueError:
            print("Entrada no válida. Introduce un entero.")

    posiciones = [i + 1 for i, v in enumerate(lista) if v == objetivo]
    if posiciones:
        print(f"El número {objetivo} aparece en las posiciones: {', '.join(map(str, posiciones))}")
    else:
        print(f"El número {objetivo} no aparece en la lista.")

if __name__ == "__main__":
    main()