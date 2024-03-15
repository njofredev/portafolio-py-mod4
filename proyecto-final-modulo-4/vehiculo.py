"""
Proyecto final módulo 4 - "Creación de una clase vehículo"
Nicolás Jofré Andrade

- Crea un archivo llamado vehiculo.py
- Definir clase llamada Vehiculo
    - Atributos: marca, modelo, color y velocidad
    - Métodos: acelerar() - Aumenta velocidad en 10 unidades
               frenar() - Disminuye velocidad en 5 unidades

- Imprimir estado del vehículo después de cada método
"""
# Clase de vehículo
class Vehiculo:

    def __init__(self, marca, modelo, color, velocidad, velocidad_actual):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
        self.velocidad_actual = velocidad_actual
    
    def datos_actuales(self):
        print(f"Los datos del auto son: {self.marca}/{self.modelo}/{self.color}/va a:{self.velocidad_actual}km/h")

    def acelerar(self):
        self.velocidad += 10
        print(f"El auto marca: {self.marca}, modelo: {self.modelo}, color: {self.color} va a: {self.velocidad}km/h")
        
    def frenar(self):
        self.velocidad -= 5
        print(f"El auto marca: {self.marca}, modelo: {self.modelo}, color: {self.color} va a: {self.velocidad}km/h")

vehiculo = Vehiculo("BMW", "X4", "Negro", 0, 0)

vehiculo.datos_actuales()