# EJERCICIO DE CODIFICACIÓN 118 Práctica Clases 1
""" 
Crea una clase llamada Personaje (todavía sin contenido: usa pass ). A continuación,
crea un objeto de esa clase llamado heroe e imprime su tipo con print(type(heroe))
para comprobar que Python reconoce tu nueva creación.
"""
class Personaje:
    pass
heroe = Personaje()
print(type(heroe))

#pass· rellena lo que falta en la clase 

#Ejercicio 119
# EJERCICIO DE CODIFICACIÓN 119 Práctica Clases 2
""" 
Crea una clase Coche cuyo constructor reciba marca y modelo y los guarde como
atributos. Instancia un coche de tu marca favorita y muestra por pantalla una frase como:
"Mi coche es un Toyota Corolla"
"""


# EJERCICIO DE CODIFICACIÓN 120 Práctica Clases 3
""" 
Crea una clase Libro con los atributos titulo y autor . Crea dos libros distintos a
partir del mismo molde e imprime los datos de cada uno. Fíjate bien: dos objetos, una sola
clase. Ese es el superpoder que acabas de desbloquear.
"""



# EJERCICIO DE CODIFICACIÓN 121 Práctica Atributos 1
""" 
Crea una clase Mascota con un atributo de clase especie = "desconocida" y un
constructor que guarde nombre y edad como atributos de instancia. Crea una mascota e
imprime sus tres atributos
"""

# EJERCICIO DE CODIFICACIÓN 122 Práctica Atributos 2
""" 
Crea una clase CuentaBancaria cuyo constructor reciba el titular y asigne un saldo
inicial de 0 por defecto. Abre una cuenta a nombre de "Dirceu", deposita mentalmente tu
emoción y muestra el saldo por pantalla (spoiler: será 0, pero es tu 0).
"""
class CuentaBancaria:
    titular =""
    saldo = 0
    def __init__(self,titular):
        self

