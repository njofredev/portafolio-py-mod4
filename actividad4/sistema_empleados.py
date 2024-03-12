"""
Actividad n°4 "Sistema de empleados"
Nicolás Jofré Andrade

- Crea un archivo llamado sistema_empleados.py
- Implementar un programa que modele un sistema de empleados utilizando herencia y 
polimorfismo en Python. Crear clases como: empleado, departamento y clases derivadas
como: desarrollador y gerente que hereden de empleado.
"""
# Definición de clases
class Empleado:

    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

    def modificar_datos(self):
        empleados = []
        self.id = input("Ingrese el ID del empleado: ")
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.apellido = input("Ingrese el apellido del empleado: ")

        for e in empleados:
            empleados.append(self.id)
            empleados.append(self.nombre)
            empleados.append(self.apellido)

    def mostrar_datos(self):
        return print(f"Hola, soy el empleado {self.id}, mi nombre es: {self.nombre} y mi apellido es: {self.apellido}")
    
class Departamento(Empleado):

    def __init__(self, empleado, nombre_departamento):
        super().__init__(id, empleado, nombre_departamento)
        self.nombre_departamento = nombre_departamento

    def mostrar_datos(self):
        return print(f"el departamento es: {self.nombre_departamento}.")
    
class Desarrollador(Empleado):

    def __init__(self, id, nombre, apellido, lenguaje_favorito):
        super().__init__(id, nombre, apellido, lenguaje_favorito)
        self.lenguaje_favorito = lenguaje_favorito

    def mostrar_datos(self):
        return print(super().Saludar())

class Gerente(Empleado):

    def __init__(self, id, nombre, apellido, empleados_a_cargo):
        super().__init__(id, nombre, apellido, empleados_a_cargo)
        self.empleados_a_cargo = empleados_a_cargo

empleado_1 = Empleado("001", "Nicolás", "Jofré")
departamento_1 = Departamento(Empleado, "Desarrollo")
departamento_2 = Departamento(Empleado, "Gerencia")

# Menú e instancias
empleados = []
while True:
    print("\n***Sistema de empleados***")
    print("(1) Agregue un empleado")
    print("(2) Ver datos de empleados")
    print("(3) Modificar datos de empleado")
    print("(4) Salir del programa")
    opcion_menu = int(input("Ingrese un valor del menú: "))

    if opcion_menu == 1:
        cantidad = int(input("Ingrese la cantidad de empleados: "))
        for i in range(empleados):
            pass
    elif opcion_menu == 2:
        pass
    elif opcion_menu == 3:
        pass
    elif opcion_menu == 4:
        pass
    else:
        print("ERROR: Ingrese un valor válido del menú...")
