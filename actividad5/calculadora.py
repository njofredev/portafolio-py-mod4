"""
Actividad n°5 "Calculadora"
Nicolás Jofré Andrade

- Crea un archivo llamado calculadora.py
- Implementar una calculadora simple en python que maneje errores y excepciones. Debe
realizar operaciones básicas como: suma, resta, multiplicación y división. Debe manejar
errores y excepciones como la división por 0 y la entrada incorrecta del usuario.
- metas: usar assert() e isinstance() para la comprobación de erorres
"""
"""class Calculadora:
    
    def __init__(self, operacion):
        self.operacion = operacion""" # Suma, resta, multiplicacion, division
        
class Operacion:
    
    def __init__(self, num_1, num_2, operacion, resultado):
        self.num_1 = num_1
        self.num_2 = num_2
        self.operacion = operacion
        self.resultado = resultado
    
    def sumar(self):
        self.num_1 = int(input("Ingrese el primero número: \n"))
        self.num_2 = int(input("Ingrese el segundo número: \n"))

        print(f"La suma de {self.num_1} y {self.num_2} es: {self.num_1 + self.num_2}")

    def restar(self, a, b):
        pass

    def multiplicar(self, a, b):
        pass

    def dividir(self, a, b):
        pass

calculadora = Operacion(1, 2, "suma", 3)

calculadora.sumar()