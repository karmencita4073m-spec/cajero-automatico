# EJERCICIO DE CODIFICACIÓN 130 #Práctica Herencia
# Crea una clase Vehiculo con un atributo marca. Después crea una clase Moto que herede
# de Vehiculo sin añadir nada (usa pass). Instancia una moto, dale una marca e
# imprímela. Si funciona, acabas de heredar por primera vez.
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca


class Moto(Vehiculo):
    pass


moto = Moto("Motomami")
print(f"Marca de moto: {moto.marca}")


## EJERCICIO DE CODIFICACIÓN 131 - Práctica Herencia 2
# Partiendo de tu CuentaBancaria (titular, saldo, depositar()), crea
# cuentaAhorro(CuentaBancaria) con un método exclusivo aplicar_interes(tasa) que
# incremente el saldo según la tasa indicada. Demuestra que la hija puede depositar y
# aplicar intereses.

class BankAccount:
    # Atributos
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Transacción correcta: Has depositado {amount} €. Tu saldo actual es de: {self.balance} €")
    
class SavingsAccount(BankAccount):
    def apply_interest(self, rate):
        self.balance +=  self.balance * rate
        
# Cuenta ahorro
account_1 = SavingsAccount("Kelvin", 20000)
print(f"Saldo sin aplicar interéa: {account_1.balance:.2f} €")
# Depositar dinero
account_1.deposit(5000)
print(f"Saldo tras depósito sin aplicar interés: {account_1.balance:.2f} €")
# Aplicar interés
account_1.apply_interest(0.02)
print(f"Saldo con interés 0.02: {account_1.balance:.2f} €")


## EJERCICIO DE CODIFICACIÓN 132 - Práctica Herencia 3

class Ave:
    def cantar(self):
        print("El ave canta")


class Canario(Ave):
    def cantar(self):
        print("El canario trina")


Ave().cantar()
Canario().cantar()



# Paso 1: La clase base Superheroe
#Crea una clase Superheroe con:
#Atributos: nombre, energia (empieza en 100)
#Método presentarse() → imprime: "¡Soy {nombre} y mi energía es {energia}!"Método usar_poder() → imprime "Uso mi poder genérico..." y resta 10 de energía
#Método recargar() → energía vuelve a 100 e imprime "¡Energía al máximo!

# Paso 1: La clase base Superheroe
class Superheroe:
    def __init__(self, nombre, energia=100):
        self.nombre = nombre
        self.energia = energia

    def presentarse(self):
        print(f"¡Soy {self.nombre} y mi energía es {self.energia}!")

    def usar_poder(self):
        print("Uso mi poder genérico...")
        self.energia -= 10

    def recargar(self):
        self.energia = 100
        print("¡Energía al máximo!")
        
#FASE 2
        
       #🦸 Paso 2: Los héroes hijos
#Crea 3 clases que hereden de Superheroe. Cada una debe sobrescribir usar_poder() con su propio estilo:
#🕷️ HombreAracnido
#Al usar su poder imprime: "¡Lanzo telaraña! 🕸️" y gasta 15 de energía.
#🔥 ChicaFuego
#Al usar su poder imprime: "¡Bola de fuego! 🔥" y gasta 25 de energía.
#xtra: método calentar_comida() que imprime "Pizza calentita 🍕" (¡no gasta energía!)
#🧊 ChicoHielo
#Al usar su poder imprime: "¡Rayo congelante! ❄️" y gasta 20 de energía. 
class HombreAracnido(Superheroe):
    def usarpoder(self):
        self.nombre =  HombreAracnido
        self.energia = 100
        print(f"Yo soy {self.nombre} y  mi energis es de {self.energia}")
        def usar_poder(self):
            print(f"Y ¡Lanzo telaraña")
        self.energia = -15
        class Chicafuego(Superheroe):
            def usar_poder(self):
                self.nombre = Chicafuego
                self.energia = 100
                print(f"Me llamo {self.nombre} y tengo energia {self.energia}")
                def usar_poder(self)
                print(f"¡Bola de Fuego")
                self.energia = - 25
                def calentar_comida(self):
                    print(f"Pizza Calentita")
                    self.energia = 0
                
class Chicohielo(Superheroe):      
    def usar_poder(self):
        self.nombre = Chicohielo
        self.energia = 100
        def usar_poder(self):
                    print(f"Soy {self.nombre} y tengo {self.energia}")
        def usar_poder(self):
            print(f"Rayo congelante")
            self.energia = -20
#Paso 3: El modo entrenamiento
#Crea una función entrenar(heroe, veces) que:
#1. Llame a presentarse()
#2. Use su poder veces veces seguidas
#3. Si la energía llega a 0 o menos, imprima "{nombre} se quedó sin energía ç



# Paso 4: ¡El torneo!

#Crea una lista con un objeto de cada héroe y haz que cada uno entrene 5 veces con su poder. 
# Al final imprime quién terminó con más energía.



#EJERCICIO 