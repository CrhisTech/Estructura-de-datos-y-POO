# Módulo main.py

from Paquete_Mensajeria.Mensajeria import *
from Paquete_Trigonometricas.Trigonometricas import *
from Paquete_Basicas.Basicas import *
from Paquete_Lecturas.Lecturas import *


# Programa principal (llamada de métodos)
Mensajes("Bienvenido a la aplicación")
x=LeerA()
y=LeerB()

Mensajes("Operaciones básicas")
print("Suma         :", Suma(x,y))
print("Resta        :", Resta(x,y))
print("Multipliación:", Multiplicar(x,y))
print("División         :", Division(x,y))

Mensajes("Operaciones trigonométricas")
print("Seno         :", Seno(x))
print("Coseno       :", Coseno(x))
print("Raiz Cuadrada:", Raiz_Cuadrada(x))
Mensajes("Gracias por usar la aplicación!")
