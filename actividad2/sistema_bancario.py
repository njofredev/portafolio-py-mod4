"""
Actividad n°2 "Sistema bancario"
Nicolás Jofré Andrade

- Crea un archivo llamado sistema_bancario.py
- Implementa un programa que modele un sistema bancario utilizando POO. Crear clases
que representen cuentas bancarias y clientes con atributos como: saldo, nombre titular 
y métodos para realizar transacciones.
"""
class Cuentabancaria:

    def __init__(self, nro_cuenta, saldo):
        self.nro_cuenta = nro_cuenta
        self.saldo = saldo

    def mostrarSaldo(self):
        return f"El saldo actual de la cuenta {self.nro_cuenta} es: {self.saldo}"

class Cliente(Cuentabancaria):
    def __init__(self, nro_cuenta, saldo, rut, nombre):
        super().__init__(nro_cuenta, saldo)
        self.rut = rut
        self.nombre = nombre
        
    def mostrar_datos_usuario(self):
        return f"La cuenta de {self.nombre} es: {self.nro_cuenta}, su rut: {self.rut} y tiene: {self.saldo}$.- en la cuenta. \n"
    
    def depositar(self):
        ingreso = int(input("Ingrese la cantidad: \n$"))
        self.saldo += ingreso
        return f"${ingreso}.- ingresados correctamente"
            
    def retirar(self):
        retiro = int(input("Ingrese la cantidad a retirar: \n$"))
    
        if retiro < 0 or retiro > self.saldo :
            return f"ERROR: Ingrese una cantidad mayor a su saldo. Su saldo actual es: {self.saldo}"
        else:
            self.saldo -= retiro
            return f"${retiro}.- retirados correctamente"
                     
# Operaciones del programa
# Clases anidadas
cliente1 = Cliente("12345", 0, "19.258.679-8", "Nicolás J.")

# Llamado de métodos con menú
while True:
    print("--- Sistema bancario --- \n")
    print("1. Ver datos del usuario")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir del programa \n")

    opcionMenu = int(input("Ingrese una opción del menú: \n"))

    if opcionMenu == 1:
        print(cliente1.mostrar_datos_usuario())
    elif opcionMenu == 2:
        print(cliente1.depositar())
    elif opcionMenu == 3:
        print(cliente1.retirar())
    elif opcionMenu == 4:
        print("Gracias por participar!")
        break
    else:
        print("ERROR: Ingrese un valor correspondiente al menú")