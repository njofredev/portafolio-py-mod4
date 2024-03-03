"""
Actividad n°1 "Orientación a objetos en Python"
Nicolás Jofré Andrade

- Crea un archivo llamado gestion_estudiantes.py
- Implementar un programa para estudiantes:
    - Crear clase Estudiante
        - Atributos: nombre, edad y calificaciones.
        - Métodos: cambiarDatos(), calcularPromedio()
"""
# Clase estudiante
class Estudiante:
    
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones
        
    def cambiarDatos(self):
        nuevo_nombre = str(input("Ingrese un nuevo nombre de usuario: \n"))
        self.nombre = nuevo_nombre
        nueva_edad = int(input("Ingrese una nueva edad: \n"))
        self.edad = nueva_edad
        
        cant_calificaciones = int(input("Ingrese la cantidad de notas a cambiar: "))
        cali = []
        for n in range(cant_calificaciones):
            nota = float(input(f"Ingrese la nota°{n + 1}: \n"))
            cali.append(nota)
        self.calificaciones = cali    
        print(f"El nuevo nombre es: {self.nombre}, la nueva edad es: {self.edad} y las nuevas calificaciones son: {self.calificaciones}")
        
    def calcularPromedio(self, calificaciones):
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"Las notas actuales del usuario son: {calificaciones}")
        print(f"El promedio de las notas ingresadas es: {promedio}")
        
estudiante1 = Estudiante("Nicolás", 27, 7.7)
print(f"Los datos anteriores del estudiante son: nombre: {estudiante1.nombre} - edad: {estudiante1.edad} - notas: {estudiante1.calificaciones}")
estudiante1.cambiarDatos()
estudiante1.calcularPromedio(estudiante1.calificaciones)
