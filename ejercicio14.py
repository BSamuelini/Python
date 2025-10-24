nombres = input("Escribe varios numeros separados por comas: ")

lista_nombres = []
for nombre in nombres.split(','):
    nombre_limpio = nombre.strip()
    if nombre_limpio:
        lista_nombres.append(nombre_limpio)

lista_nombres.reverse()

print("\nNombres en orden invertido:", ", ".join(lista_nombres))