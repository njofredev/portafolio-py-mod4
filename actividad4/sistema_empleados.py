"""
Actividad n°4 "Sistema de empleados"
Nicolás Jofré Andrade

- Crea un archivo llamado sistema_emepleados.py
- Implementar un programa que modele un sistema de empleados utilizando herencia y 
polimorfismo en Python. Crear clases como: empleado, departamento y clases derivadas
como: desarrollador y gerente que hereden de empleado.
"""
# Definición de clases
class Empleado:
    
    def __init__(self, nombre, apellido, departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.departamento = departamento

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.departamento})"

    def get_nombre_empleado(self):
        return f"{self.nombre} {self.apellido}"

    def get_departamento(self):
        return self.departamento

class Departamento:
        
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Desarrollador(Empleado): # Herencia de Empleado
    
    def __init__(self, nombre, apellido, departamento, lenguaje_favorito):
        super().__init__(nombre, apellido, departamento)
        self.lenguaje_favorito = lenguaje_favorito

    def __str__(self): # Presentación informal del objeto con __str__ y __repr__ para una presentación formal
        return f"{super().__str__()} - Lenguaje favorito: {self.lenguaje_favorito}"

class Gerente(Empleado):
    def __init__(self, nombre, apellido, departamento, empleados_a_cargo):
        super().__init__(nombre, apellido, departamento)
        self.empleados_a_cargo = empleados_a_cargo

    def __str__(self):
        return f"{super().__str__()} - Tiene a cargo: {len(self.empleados_a_cargo)} personas."

# Se generan 2 departamentos
departamento_desarrollo = Departamento("Desarrollo")
departamento_gerencia = Departamento("Gerencia")

# Se generan 2 empleados
empleado1 = Desarrollador("Juan", "Pérez", departamento_desarrollo, "Python")
empleado2 = Gerente("María", "Gómez", departamento_gerencia, [empleado1])

print(empleado1)
print(empleado2)  
