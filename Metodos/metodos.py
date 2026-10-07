
#Si los atributos son lo que un objeto tiene, los métodos son lo que un objeto sabe hacer.
#Técnicamente son funciones, pero viven dentro de una clase y su primer parámetro es siempre
#self , el pase VIP que les permite tocar los atributos del objeto
#"""
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, monto):
        self.saldo += monto
        print(f"Deposito ok, Nuevo saldo : {self.saldo} €")
        
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro ok: Nuevo saldo {self.saldo} €")  
        else:
            print("Fondos insuficientes : El Banco no regala dinero")
            
cuenta = CuentaBancaria("Juan", 50000)
cuenta2= cuenta
cuenta.depositar(50)  
cuenta.retirar(250)   
cuenta.retirar(5000000)



#Se desea modelar un punto en el plano cartesiano mediante una clase llamada Punto. Cada objeto de esta clase debe almacenar dos coordenadas: x e y.
#Se pide:
#fine la clase Punto con un método constructor (__init__) que reciba como parámetros los valores iniciales de x e y, y los asigne como atributos del objeto.Crea dos objetos de la clase Punto:
#con coordenadas (2, 5
# 2 con coordenadas (9, 1)
#difica únicamente la coordenada x del objeto p1, asignándole el valor 100.
#prime por pantalla las coordenadas de ambos puntos.
#sponde: ¿Por qué al modificar p1.x no se ve afectado p2.x? ¿Qué concepto de la programación ori_ntada a objetos se pone de manifiesto?

class Punto:
   def __init__(self,x,y):
       self.x = x
       self.y = y
       p1 = Punto(2,5)
       p2 = Punto(9,1)
       p1 = 100
       print(f"p1: {p1.x} {p1.y}")
       #Porque al modificar p1 p2 no se ve afectado ya que hemos creados dos objertos difer
       
##EJERCICIO DE CODIFICACIÓN 124 Práctica Métodos 1
""" 
#Crea una clase Lapiz con un método escribir(texto) que imprima: "El lápiz escribe:
#[texto]". Crea un lápiz y ponlo a trabajar
#"""
class Lapiz:
    def escribir(self,texto):
        print(f"El lápiz escribe : texto")
        lapiz = Lapiz()
        Lapiz.escribir("Hola, soy un lápiz y estoy escribiendo")
        
    
 # EJERCICIO DE CODIFICACIÓN 125 Práctica Métodos 2
""" #Dta a tu clase CuentaBancaria de un método depositar(monto) que sume el monto al
#aldo y muestre el nuevo saldo. Abre una cuenta con 100 €, deposita 40 € y comprueba el
#sultado.

"""

class CuentaBancaria:
    def __init__(self,titular,saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, monto):
        self.saldo += monto
        cuenta = CuentaBancaria("juan", 100)
        cuenta.depositar(40)
        depositar(40)
        def depositar(self.monto + sel.saldo):
            print(f"Deposito ok, Nuevo saldo : {self.saldo} €")
            
            
#EJERCICIO DE CODIFICACIÓN 126 Práctica Métodos 3
#Crea una clase Contador que empiece en 0, con dos métodos: incrementar() (suma 1) y
#reiniciar() (vuelve a 0). Incrementa tres veces, muestra el valor, reinicia y vuelve a
#ostrarlo. Pequeño programa, gran concepto: los métodos cambian el estado del
#objeto

class Contador:
    def __init__(self):
        self.valor = 0
    def incrementar(self):
        self.valor += 1
        def reiniciar(self):
            self.valor = 0
        contador = Contador()
        contador.incrementar()
        contador.incrementar()
        contador.incrementar()
        print(contador.valor)
        contador.reiniciar()
        print(contador.valor)
        
        ## EJERCICIO DE CODIFICACIÓN 127 Práctica Tipos de Métodos 1
#""" 
#Crea una clase Estudiante con nombre y curso , y un método de instancia
#presentarse() que imprima: "Hola, soy [nombre] y estoy en [curso]". Haz que un
#estudiante se presente.
class Estudiante:
    def __init__(self.nombre,curso):
        self.nombre = "nombre"
        self.curso = "curso"
        def presentarse(self):
            print(f"Hola, soy {self.nombre} y estoy en {self.curso}")
            estudiante = Estudiante("kharmen", "Desarollo de software")
            estudiante.presentarse()
            print(estudiante.nombre, estudiante.curso)
            
            
 #       # EJERCICIO DE CODIFICACIÓN 128 Práctica Tipos de Métodos 2
#""
#Crea una clase Banco con un atributo de clase tasa_interes = 0.02 y un método de clase
#actualizar_tasa(nueva) . Cambia la tasa a 0.05 llamando al método desde la clase (sin
#crear objetos) e imprime el nuevo valor 
#""

class Banco:
   #Creamos la clase BANCO y un atributo tasa_de_interes
    tasa_interes = 0.02
    @classmethod
    def actualizar_tasa(cls,nueva):
     
     cls.tasa_interes = nueva_tasa

    # Método estático → validar cantidad
    @staticmethod
    def es_monto_valido(monto):
        return monto > 0


# ==========================================
# Ejecución paso a paso
# ==========================================

# 1. Crear cuenta
cuenta1 = CuentaBancaria("Kevin", 20000)

# 2. Calcular interés ANTES de cambiar la tasa
interes_ganado = cuenta1.saldo * cuenta1.tasa_interes
print(f"Interés calculado con tasa inicial: {interes_ganado}")

# 3. CAMBIAR tasa → afecta a TODAS las cuentas
CuentaBancaria.cambiar_tasa(0.03)

# 4. Validación sin crear cuenta → -50 no es válido
print(CuentaBancaria.es_monto_valido(-50))  # False 

# 5. Mostrar datos
print(cuenta1.titular, cuenta1.saldo)       # Kevin 20000 
print(cuenta1.tasa_interes)                 # 0.03 → ya se actualizó 

# 6. Saldo total con interés
print(f"Su saldo con interés: {cuenta1.saldo + interes_ganado}")
     
    
### EJERCICIO DE CODIFICACIÓN 129 Práctica Tipos de Métodos 3
## EJERCICIO DE CODIFICACIÓN 129 Práctica Tipos de Métodos 3
#Añade a la clase Banco anterior un método estático es_monto_valido(monto) que
#devuelva True si el monto es ma yor que cero. Pruébalo con 200 y con -10 , todo sin
#instanciar nada.
class Banco:
    @staticmethod
    def es_monto_valido(monto):
    return < 0
print()
    
    
    
    
#    