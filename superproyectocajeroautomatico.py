#Todos los apartados del ejercicio deben estar hechos.
#Crear programa simulador de un cajero autimatico por dentro.
#Requisitos:
#Clase Persona: atributos con nombre y apellidos(El titular de la cuenta)
#Clase Cuenta: atributos clientes(una persona) y saldo(comenzando en cero)
#Debe incluir: Metodo especial - str muestra datos de forma amigable
#Un metodo depositar monto que sume dinero al saldo rechazando montos de cero o negativo.
#Programa principal al arrancar pide al usuario su nombre completo,
#le da la bienvenidad con los datos de su cuenta y le ofrece un menu en bucle.
#depositar dinero
#retirar dinero
#salir con un mensaje de despedida y el saldo final.
#El menu debe repetirse hasta que el ususario elija salir 
#y debe avisar con educacion pero con firmeza cuando una operacion no es posible.
#Pistas:Convierte la entrada del usuario a float para poder trabajar con decimales. float(input)
#Bucle while con una opcion elegida por eñ usuario y if , elif, y
#else para dirigirse a cada opcion.
#Deberá imprimir el saldo despues de cada operacion.


#Creando la clase persona con datos de un cliente. Self hace alusion en ingles a uno mismo.
class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
#Creamos la clase Cuenta Corriente con los correspondientes atributos de clente y saldo a 0
class Cuentacorriente():
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo
    
    def __str__(self):
        return f"{self.cliente.nombre} {self.cliente.apellidos}  {self.saldo}"
    #Ponemos return para que nos imprima los datos del tirular de la cuenta y el saldo. Luego una funcion que permita al cliente depositar dinero en la cuenta.
    def depositar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        else:
            return False
    #Si el dinero que se ingresa es  mayor o igual a cero return nos devolvera True. En caso contrario Flase
    def retirar_dinero(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        else:
            return False
#Necesitamos crear una funcion que nos permita obtener el saldo de la cuenta
    def obtener_saldo(self):
        return self.saldo
#En este punto lo quue al principio fue poner este coddigo al principio del todo. Pero resulta que no era ahi donde iba sino aqui
nombreCompleto = input("Introduce tu nombre y apellidos: ")
nombre, apellidos = nombreCompleto.split(" ", 1)
persona = Persona(nombre, apellidos)
banco = Cuentacorriente(persona)
self = cliente = persona
self = saldo = banco.obtener_saldo()
#Ahora damos la bienvenida con un saludo a la persoona con dos primte diferentes. En uno lsaludamos, en otro mostramos la cuenta
print(f"¡Hola! Gusto de saludarte: {nombreCompleto}")
print(f"Tu cuenta: {banco}")
#Como vamos a ofrecer una serie de opciones en  el cajero con un menu y desconocemos cuantas veces tendra que ejecutarse el bucle, usamos un while.
while True:
    opciones = """"""
#Mostramos las opciones al cliente para que escoja una.
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Salir")
    opcion = input("Selecciona una opcion: ")
    ("_" * 40)
    if opcion == "1":
        dinero = float(input("¿Cuanto desea depositar? "))
        if banco.depositar_dinero(dinero):
            print("Ingreso exitoso")
            print(f"Su saldo ahora es de: ${banco.obtener_saldo():.2f}")
        else:
            print("No se pudo realizar la operacion. Intente de nuevo")
    elif opcion == "2":
        dinero = float(input("Introduzca la cantidad que desea retirar: "))
        if banco.retirar_dinero(dinero):
            print("La cantidad ha sido retirada con exito.")
            print(f"Su saldo actual es de: ${banco.obtener_saldo():.2f}")
        else:
            print("No se puede realizar la operacion. Fondos insuficientes.")
            print(f"Su saldo actual es: ${banco.obtener_saldo():.2f}")
    elif opcion == "3":
        print("Gracias por su visita")
        print(f"Saldo final: ${banco.obtener_saldo():.2f}")
        break
    else:
        print("Opcion no valida. Intente de nuevo")
