"""
Actividad n°5 "Calculadora"
Nicolás Jofré Andrade

- Crea un archivo llamado calculadora.py
- Implementar una calculadora simple en python que maneje errores y excepciones. Debe
realizar operaciones básicas como: suma, resta, multiplicación y división. Debe manejar
errores y excepciones como la división por 0 y la entrada incorrecta del usuario.
"""     
class Operacion:
    
    def __init__(self):
        pass
    
    def sumar(self):
        while True:
            try:
                self.num_1 = int(input("Ingrese el primer número: \n"))
                self.num_2 = int(input("Ingrese el segundo número: \n"))

                print(f"La suma de {self.num_1} y {self.num_2} es: {self.num_1 + self.num_2}")
                break
            except ValueError:
                print("ERROR: Ingrese un valor numérico válido.")
                break

    def restar(self):
        while True:
            try:
                self.num_1 = int(input("Ingrese el primer número: \n"))
                self.num_2 = int(input("Ingrese el segundo número: \n"))

                print(f"La resta de {self.num_1} y {self.num_2} es: {self.num_1 - self.num_2}")
                break
            except ValueError:
                print("ERROR: Ingrese un valor numérico válido.")
                break

    def multiplicar(self):
        while True:
            try:
                self.num_1 = int(input("Ingrese el primer número: \n"))
                self.num_2 = int(input("Ingrese el segundo número: \n"))

                print(f"La multiplicación de {self.num_1} y {self.num_2} es: {self.num_1 * self.num_2}")
                break
            except ValueError:
                print("ERROR: Ingrese un valor numérico válido.")
                break

    def dividir(self):
        while True:
            try:
                self.num_1 = int(input("Ingrese el primero número: \n"))
                self.num_2 = int(input("Ingrese el segundo número: \n"))

                print(f"La división entre {self.num_1} y {self.num_2} es: {self.num_1 / self.num_2}")
                break
            except ZeroDivisionError:
                print("ERROR: Está intentando dividir por 0.")
                break
        
# Instancia de la clase
calculadora = Operacion()            

while True:
    print("\n---Calculadora básica---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir del programa")
    opcion_menu = int(input("Ingrese una opción del menú: \n"))

    if opcion_menu == 1:
        calculadora.sumar()
    elif opcion_menu == 2:
        calculadora.restar()
    elif opcion_menu == 3:
        calculadora.multiplicar()
    elif opcion_menu == 4:
        calculadora.dividir()
    elif opcion_menu == 5:
        print("Gracias por participar en la calculadora. Saliendo..")
        break
    else:
        print("ERROR: Ingrese un valor del menú.")
