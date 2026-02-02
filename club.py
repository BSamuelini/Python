class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = None

    def añadir_equipo(self, equipo):
        if self.equipo:
            self.equipo.jugadores_eq.remove(self)
        self.equipo = equipo
        equipo.añadir_jugador(self) 
    
    def mostrar(self):
        if self.equipo:
            print(f"{self.dorsal}. {self.nombre}: {self.equipo.nombre_equipo}")
        else:
            print(f"{self.dorsal}. {self.nombre}: Sin equipo")
    
class Equipo:
    def __init__(self, nom_eq):
        self.nombre_equipo = nom_eq
        self.jugadores_eq = []

    def añadir_jugador(self, jugador):  
        if jugador not in self.jugadores_eq:
            self.jugadores_eq.append(jugador)

    def mostrar_jugadores(self):
        if not self.jugadores_eq:
            print(f"El equipo {self.nombre_equipo} no tiene jugadores.")
        else:
            print(f"\nJugadores del {self.nombre_equipo}:")
            for jugador in self.jugadores_eq:
                print(f"  {jugador.dorsal}. {jugador.nombre}")

# Listas globales
equipos = []
jugadores = []

# Menú principal
while True:
    print("\n=== GESTOR DE CLUB DE FÚTBOL ===")
    print("1. Crear equipo")
    print("2. Crear jugador")
    print("3. Asignar equipo a jugador")
    print("4. Listar equipos")
    print("5. Listar jugadores de un equipo")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del equipo: ")
        nuevo_equipo = Equipo(nombre)
        equipos.append(nuevo_equipo)
        print(f"Equipo '{nombre}' creado exitosamente.")
        
    elif opcion == "2":
        nombre = input("Nombre del jugador: ")
        dorsal = int(input("Dorsal del jugador: "))
        nuevo_jugador = Jugador(dorsal, nombre)
        jugadores.append(nuevo_jugador)
        print(f"Jugador '{nombre}' con dorsal {dorsal} creado exitosamente.")
        
    elif opcion == "3":
        print("\nJugadores disponibles:")
        contador = 1
        for jugador in jugadores:
            print(f"{contador}. {jugador.nombre} (dorsal {jugador.dorsal})")
            contador += 1
        
        jugador_idx = int(input("Seleccione el número del jugador: ")) - 1
        
        print("\nEquipos disponibles:")
        contador = 1
        for equipo in equipos:
            print(f"{contador}. {equipo.nombre_equipo}")
            contador += 1
        
        equipo_idx = int(input("Seleccione el número del equipo: ")) - 1
        
        jugadores[jugador_idx].añadir_equipo(equipos[equipo_idx])
        print(f"Jugador {jugadores[jugador_idx].nombre} asignado al equipo {equipos[equipo_idx].nombre_equipo}.")
        
    elif opcion == "4":
        print("\n=== LISTA DE EQUIPOS ===")
        for equipo in equipos:
            print(f"- {equipo.nombre_equipo} ({len(equipo.jugadores_eq)} jugadores)")
            
    elif opcion == "5":
        print("\nEquipos disponibles:")
        contador = 1
        for equipo in equipos:
            print(f"{contador}. {equipo.nombre_equipo}")
            contador += 1
        
        equipo_idx = int(input("Seleccione el número del equipo: ")) - 1
        equipos[equipo_idx].mostrar_jugadores()
        
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")