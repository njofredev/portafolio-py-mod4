"""
Actividad n°2 "Sistema bancario"
Nicolás Jofré Andrade

- Crea un archivo llamado sistema_bancario.py
- Implementa un programa que modele un sistema bancario utilizando POO. Crear clases
que representen cuentas bancarias y clientes con atributos como: saldo, nombre titular 
y métodos para realizar transacciones.
"""
class Cuentabancaria:

    def __init__(self, nro_cuenta, nombre, saldo):
        self.nro_cuenta = nro_cuenta
        self.nombre = nombre 
        self.saldo = saldo

    def mostrarSaldo(self):
        print(f"El usuario: {self.nombre}, su cuenta:{self.nro_cuenta}, tiene de saldo actual {self.saldo}")

class Cliente:

    def __init__(self, rut, nombre, apellido):
        self.rut = rut
        self.nombre = nombre 
        self.apellido = apellido

    def depositar(self, saldo):
        self.saldo += saldo
        return f"El saldo de {self.nombre}, Cuenta: {self.nro_cuenta}, tiene de saldo: {self.saldo}"

    def retirar(self, saldo):
        pass