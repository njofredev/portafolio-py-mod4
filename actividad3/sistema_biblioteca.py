"""
Actividad n°3 "Sistema de biblioteca (Diagrama de clases e implementación)"
Nicolás Jofré Andrade

- Crea un archivo llamado sistema_biblioteca.py
- Implementa un diagrama de clases que represente un sistema de biblioteca con libros,
autores y préstamos. Luego desarrollar una implementación básica con Python basandose
en el diagrama de clases creado.
"""
class Prestamos():
    
    def __init__(self, id_prestamo, cod_libro, cod_usuario, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.cod_libro = cod_libro
        self.cod_usuario = cod_usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        
    def obtenerPrestamo(self):
        return f"Se obtiene el prestamo"
    
    def modificarPrestamo(self):
        return f"Se modifica el prestamo"
    
    class Libro():
        
        def __init__(self, cod_libro, titulo, id_autor, categoria, año):
            self.cod_libro = cod_libro
            self.titulo = titulo
            self.id_autor = id_autor
            self.categoria = categoria
            self.año = año
            
        def obtenerDatos(self):
            f"Se obtienen los datos del libro"
        
        def modificarLibro(self):
            f"Se modifican los datos del libro"
    
        class Autor():
            
            def __init__(self, id_autor, nombre, nacionalidad, fecha_nacimiento, cant_libro_escritos):
                self.id_autor = id_autor
                self.nombre = nombre
                self.nacionalidad = nacionalidad
                self.fecha_nacimiento = fecha_nacimiento
                self.cant_libros_escritor = cant_libro_escritos
                
            def agregarLibro(self):
                f"Se agrega un libro nuevo"

# Implementación de diagrama de clases sistema_bibliote.pdf a Python con clases anidadas.