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

    def __init__(self, id, nombre, apellido, cargo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo

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
    
class Departamento(Empleado): # Nombre de departamento

    def __init__(self, id, nombre, apellido, cargo, nombre_departamento):
        super().__init__(id, nombre, apellido, cargo, nombre_departamento)
        self.nombre_departamento = nombre_departamento

    def mostrar_datos(self):
        return print(f"el departamento es: {self.nombre_departamento}.")
    
class Desarrollador(Empleado):

    def __init__(self, id, nombre, apellido, cargo, lenguaje_favorito):
        super().__init__(id, nombre, apellido, cargo, lenguaje_favorito)
        self.lenguaje_favorito = lenguaje_favorito

    def mostrar_datos(self):
        return print(f"los datos del desarrollador son: ")

class Gerente(Empleado):

    def __init__(self, id, nombre, apellido, empleados_a_cargo):
        super().__init__(id, nombre, apellido, empleados_a_cargo)
        self.empleados_a_cargo = empleados_a_cargo

empleado_1 = Empleado("001", "Nicolás", "Jofré", "Desarrollador")
empleado_2 = Empleado("002", "Pedro", "Aniz", "Gerente")

print(f"Los datos de empleado son: {empleado_1.id}/{empleado_1.nombre}/{empleado_1.apellido}/{empleado_1.cargo}")
print(f"Los datos de empleado son: {empleado_2.id}/{empleado_2.nombre}/{empleado_2.apellido}/{empleado_2.cargo}")

