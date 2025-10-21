print("Introduce una edad:")
edad = int(input())
if edad <= 0 or edad > 120:
    print("Edad no válida")
elif edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
