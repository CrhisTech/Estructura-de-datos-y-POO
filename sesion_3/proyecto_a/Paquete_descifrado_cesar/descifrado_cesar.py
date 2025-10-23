# Modulo: descifrado_cesar

def Descifrado_Cesar(Cifrado):
    Mensaje=""
    for Caracter in Cifrado:
        if not Caracter.isalpha():
            continue
        Caracter = Caracter.upper()
        Codigo = ord(Caracter)-1
        if Codigo < ord("A"):
            Codigo = ord("Z")
        Mensaje += chr(Codigo)
    return Mensaje
