# EJERCICIO DE CODIFICACIÓN 133 Práctica Herencia Extendida 1

# Crea CuentaCorriente(CuentaBancaria) con un constructor que use super().__init__()
# para titular y saldo, y que añada limite_descubierto. Abre una cuenta corriente e
# imprime sus tres atributos.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, limite_descubierto):
        super().__init__(titular, saldo)
        self.limite_descubierto = limite_descubierto


cuenta = CuentaCorriente("Ana", 1500, 500)
print(cuenta.titular)
print(cuenta.saldo)
print(cuenta.limite_descubierto)
    
    
    
#EJERCICIO DE CODIFICACIÓN 134 Práctica Herencia Extendida 2

#Sobrescribe el método retirar(monto) en CuentaCorriente para que permita quedarse
#en negativo hasta el limite_descubierto . Pruébalo retirando una cantidad mayor que el
#saldo pero menor que saldo + límite.


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, limite_descubierto):
        super().__init__(titular, saldo)
        self.limite_descubierto = limite_descubierto


cuenta = CuentaCorriente("Ana", 1500, 500)
print(cuenta.titular)
print(cuenta.saldo)
print(cuenta.limite_descubierto)
    
del retirar(self,monto)






## EJERCICIO DE CODIFICACIÓN 135 Práctica Herencia Extendida 3
""" 
Crea las clases Nadador (método nadar() ) y Volador (método volar() ), y una clase
Pato que herede de ambas. Crea un pato y haz que nade y vuele. Bonus: imprime
Pato.__mro__ y descubre el orden de búsqueda.
"""


class Nadador():
        self.nombre = Lucas
            def nadar(): 
                    def volar():
                        class Pato(Nadador):
                            def volar():
                             def nadar():