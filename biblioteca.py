class Libro:
    #Libro con título y autor

    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self) -> None:
        #Muestra la información del libro
        print(f"Título: {self.titulo} | Autor: {self.autor}")


class Usuario:
    #Representa un usuario de la biblioteca

    def __init__(self, nombre: str):
        self.nombre = nombre

    def mostrar_usuario(self) -> None:
        #Muestra el nombre del usuario
        print(f"Usuario: {self.nombre}")


class Biblioteca:
    #Gestión simple de una colección de libros

    def __init__(self):
        self.libros: list[Libro] = []

    def agregar_libro(self, libro: Libro) -> None:
        #Añade un libro a la biblioteca. Lanza TypeError si el objeto no es Libro.
        if not isinstance(libro, Libro):
            raise TypeError("Se esperaba un objeto de tipo Libro")
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def mostrar_libros(self) -> None:
        #Muestra todos los libros almacenados
        if not self.libros:
            print("La biblioteca no tiene libros.")
            return
        print("Libros en la biblioteca:")
        for i, libro in enumerate(self.libros, start=1):
            print(f"{i}.", end=" ")
            libro.mostrar_info()


if __name__ == "__main__":
    #Ejemplo de uso
    biblio = Biblioteca()

    #Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

    #Añadir libros
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)

    #Mostrar libros
    biblio.mostrar_libros()

    #Usuario
    usuario = Usuario("María")
    usuario.mostrar_usuario()