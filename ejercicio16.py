def pedir_entero_positivo(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Introduce un entero mayor que 0.")
        except ValueError:
            print("Entrada no válida. Introduce un entero.")

def pedir_fila(indice, N):
    while True:
        entrada = input(f"Fila {indice+1} (introduce {N} enteros separados por espacios): ").strip()
        partes = entrada.split()
        if len(partes) != N:
            print(f"Tienes que introducir exactamente {N} números.")
            continue
        try:
            return [int(x) for x in partes]
        except ValueError:
            print("Entrada no válida. Usa solo enteros.")

def main():
    N = pedir_entero_positivo("Tamaño N de la tabla (entero positivo): ")
    matriz = []
    for i in range(N):
        fila = pedir_fila(i, N)
        matriz.append(fila)

    es_identidad = True
    for i in range(N):
        for j in range(N):
            valor = matriz[i][j]
            if i == j:
                if valor != 1:
                    es_identidad = False
                    break
            else:
                if valor != 0:
                    es_identidad = False
                    break
        if not es_identidad:
            break

    if es_identidad:
        print("La tabla introducida SÍ corresponde a una matriz identidad.")
    else:
        print("La tabla introducida NO corresponde a una matriz identidad.")

if __name__ == "__main__":
    main()