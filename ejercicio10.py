# FacturaSimple.py — Plantilla (rellena los TODO)
print("=== FACTURA SIMPLE ===")

# 1) Pide N en 1..50 (usa while para validar)
# TODO: leer N y validar

N = int(input("¿Cuántas líneas de factura (1..50)? "))
while N < 1 or N > 50:
    N = int(input("Error. ¿Cuántas líneas de factura (1..50)? "))

total_bruto = 0.0
baratas = medias = caras = 0
precio_min = None
precio_max = None

# 2) Recorre 1..N con for
for i in range(1, N + 1):

    # 2.a) Precio >= 0 (validar con while)

    precio = float(input(f"Introduce el precio del producto {i}: "))
    while precio < 0:
        precio = float(input(f"Error. El precio debe ser >= 0. Introduce el precio del producto {i}: "))

    # 2.b) Cantidad >= 1 (validar con while)

    cantidad = int(input(f"Introduce la cantidad del producto {i}: "))
    while cantidad < 1:
        cantidad = int(input(f"Error. La cantidad debe ser >= 1. Introduce la cantidad del producto {i}: "))

    # 2.c) Clasifica el precio con if/elif/else y lleva contadores

    if precio < 5:
        baratas += 1
    elif precio <= 20:
        medias += 1
    else:
        caras += 1

    # 2.d) Actualiza min/max

    if precio_min is None or precio < precio_min:
        precio_min = precio
    if precio_max is None or precio > precio_max:
        precio_max = precio

    # Sumar al total bruto
    total_bruto += precio * cantidad
    

# 3) Tramos de descuento con if/elif/else

if total_bruto < 20:
    porc_desc = 0
elif total_bruto < 50:
    porc_desc = 5
elif total_bruto < 100:
    porc_desc = 10
else:
    porc_desc = 15

# 4) Calcula descuento, base, iva y total

descuento = total_bruto * porc_desc / 100 #Descuento

base = total_bruto - descuento #Base

iva = base * 21 / 100 #IVA

total = base + iva #Total

# 5) Muestra resumen con 2 decimales

print(f"Descuento: {descuento:.2f} €") #Mostrar descuento

print(f"Base: {base:.2f} €") #Mostrar base

print(f"IVA: {iva:.2f} €") #Mostrar IVA

print(f"Total: {total:.2f} €") #Mostrar total

#Baratos, medios y caros
print(f"Productos baratos: {baratas}")

print(f"Productos medios: {medias}")

print(f"Productos caros: {caras}")

#Máximo y mínimo
print(f"Precio mínimo: {precio_min:.2f} €")

print(f"Precio máximo: {precio_max:.2f} €")
