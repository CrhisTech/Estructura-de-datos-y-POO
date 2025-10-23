# Módulo main.py

from Paquete_Mensajeria.Mensajeria import *
from Paquete_OperacionesBasicas.Basicas import *
from Paquete_Promedio.Promedio import *
from Paquete_MayorMenor.MayorMenor import *
from Paquete_Lecturas.Lecturas import *
from Paquete_Trigonometricas.Trigonometricas import *

# Programa Principal (Llamada de métodos)
Mensajes("Bienvenido a la aplicación!")
x=LeerA()
y=LeerB()
z=LeerC()

Mensajes("Operaciones básicas")
print("Suma         :", Suma(x,y,z))
print("Resta        :", Resta(y,z))
print("Multipliación:", Producto(x,z))
print("División         :", Division(y,z))

Mensajes("Operaciones trigonométricas")
print("Tangente         :", Tangente(x))
print("Secante          :", Secante(z))
print("Raiz Cuadrada:", Raiz_Cuadrada(y))
print("Potencia al Cuadrado:",Potencia(y))

Mensajes("Promedio de los 3 números")
print("Promedio:", Promedio(x,y,z))

Mensajes("Número mayor:")
print(Mayor(x,y,z))
Mensajes("Número manor:")
print(Menor(x,y,z))
