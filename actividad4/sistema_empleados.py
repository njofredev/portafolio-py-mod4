"""
Actividad n°4 "Sistema de empleados"
Nicolás Jofré Andrade

- Crea un archivo llamado sistema_emepleados.py
- Implementar un programa que modele un sistema de empleados utilizando herencia y 
polimorfismo en Python. Crear clases como: empleado, departamento y clases derivadas
como: desarrollador y gerente que hereden de empleado.
"""
# Definición de clases

class Departamento: #nombre_departamento
        
    def __init__(self, nombre_departamento):
        self.nombre = nombre_departamento

    def get_departamento(self): # get datos de departamento
        print(f"El nombre del departamento es: {self.nombre_departamento}")

class Empleado(Departamento): # #nombre_departamento #id, nombre, apellido
    
    def __init__(self, nombre_departamento, id, nombre, apellido ): # Heredo nombre_departamento
        super().__init__(nombre_departamento, id, nombre, apellido)

    def get_datos_empleados(self): # get
        return print(f"{self.nombre} {self.apellido}")

    def get_departamento(self): #polimorfismo
        return self.departamento

class Desarrollador(Empleado): # Herencia de Empleado # lenguaje favorito
    
    def __init__(self, nombre, apellido, nombre_departamento, lenguaje_favorito):
        super().__init__(nombre, apellido, nombre_departamento)
        self.lenguaje_favorito = lenguaje_favorito

    def get_datos_desarrollador(self): # Presentación informal del objeto con __str__ y __repr__ para una presentación formal
        return print(f"{self.nombre} {self.apellido} {self.nombre_departamento} {self.lenguaje_favorito}")

class Gerente(Empleado): # Herencia de empleado #
    def __init__(self, nombre, apellido, departamento, empleados_a_cargo):
        super().__init__(nombre, apellido, departamento)
        self.empleados_a_cargo = empleados_a_cargo

    def __str__(self):
        return f"{super().__str__()} - Tiene a cargo: {len(self.empleados_a_cargo)} personas."

# Se generan 2 departamentos
dep_desarrollo = Departamento("Desarrollo")
dep_gerencia = Departamento("Gerencia")

# Se generan 2 empleados
empleado1 = Desarrollador("Juan", "Pérez", dep_desarrollo, "Python")
empleado2 = Gerente("María", "Gómez", dep_gerencia, [empleado1])

print(empleado1)
print(empleado2)  
