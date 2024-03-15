"""
Proyecto final módulo 4 - "Creación de una clase vehículo"
Nicolás Jofré Andrade

- Crea un archivo llamado vehiculo.py
- Definir clase llamada Vehiculo
    - Atributos: marca, modelo, color y velocidad
    - Métodos: acelerar() + Aumenta velocidad en 10 unidades
               frenar() - Disminuye velocidad en 5 unidades

- Imprimir estado del vehículo después de cada método
"""
# Clase de vehículo
class Vehiculo:

    def __init__(self, marca, modelo, color, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
    
    def datos_actuales(self):
        print(f"Los datos del auto son: Marca:{self.marca} | Modelo:{self.modelo} | Color:{self.color}| Velocidad actual: {self.velocidad}km/h")

    def acelerar(self):
        self.velocidad += 10
        print(f"El auto marca: {self.marca}, modelo: {self.modelo}, color: {self.color} va a: {self.velocidad}km/h")
        
    def frenar(self):
        if self.velocidad <= 0:
            print("El vehiculo se encuentra detenido")
        else:
            self.velocidad -= 5
            print(f"El auto marca: {self.marca}, modelo: {self.modelo}, color: {self.color} va a: {self.velocidad}km/h")

# Instancia de la clase
vehiculo = Vehiculo("BMW", "X4", "Negro", 0)

while True:
    print("Menú: \n 1. Ver datos del vehiculo\t \n 2. Acelerar auto \t \n 3. Frenar auto \t \n 4. Salir")
    opcion = int(input("Ingrese una opción del menú: "))

    if opcion == 1:
        vehiculo.datos_actuales()
    elif opcion == 2:
        vehiculo.acelerar()
    elif opcion == 3:
        vehiculo.frenar()
    elif opcion == 4:
        print("Saliendo del programa..")
        break
    else:
        print("ERROR: Ingrese un valor válido del menú.")
