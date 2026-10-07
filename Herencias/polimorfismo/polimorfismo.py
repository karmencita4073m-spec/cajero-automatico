#EJERCICIO DE CODIFICACIÓN 137 Práctica Polimorfismo 2
#Escribe una función probar_retiro(cuenta) que llame a cuenta.retirar(100) y muestre
#el saldo resultante. Pásale una CuentaBancaria con 150 € y una CuentaCorriente con 50 €
#y límite de 200 €. La misma función, dos comportamientos distintos.



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

def probar_retiro(cuenta):
    def cuenta_retirar(self):
      self.CuentaCorriente = 1500,500
cuenta.retirar = 100
print 
        
    
 #eJERCIOS
 #Crea una cñase ññamada emplerp con informe() que devuelva "Trabajo en la empresa"  y un CLASE gERERENTE CUYO INFORME() devuelva ·Dirijo un equipo".
 # EScrine una funcion publicar-informe(persona9 que imprima el inforeme de quien reciba y usala con ambos.)
 
class Empleado():
    def informe(self):
         return "Trabajo en la empresa"
class Gerente(Empleado):
         def informe(self):
             return "Dirijo un equipo"
         def publicar_informe(persona):
             print(f" {persona.informe(self)}")
                   