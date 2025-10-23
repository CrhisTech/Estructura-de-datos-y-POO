# Modulo: main.py
from Paquete_cifrado_cesar.cifrado_cesar import *
from Paquete_descifrado_cesar.descifrado_cesar import *
from Paquete_mensajeria.mensajeria import *

# Programa Principal
Mensaje("Ejemplos de Mensajes Encriptados")
M1=Cifrado_Cesar("Invadir Galia")
M2=Cifrado_Cesar("Invadir Macedonia desde Oriente")
M3=Cifrado_Cesar("Retirada")
M4=Cifrado_Cesar("Diezma al Ejercito Insurrecto")

print("Criptograma M1:", M1)
print("Criptograma M2:", M2)
print("Criptograma M3:", M3)
print("Criptograma M4:", M4)

Mensaje("Ejemplos de Mensajes Desencriptados")
print("Desencriptado M1:", Descifrado_Cesar(M1))
print("Desencriptado M2:", Descifrado_Cesar(M2))
print("Desencriptado M3:", Descifrado_Cesar(M3))
print("Desencriptado M4:", Descifrado_Cesar(M4))
