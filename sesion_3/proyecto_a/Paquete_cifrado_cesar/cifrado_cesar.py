# Modulo: cifrado_cesar

def Cifrado_Cesar(Mensaje):
    Cifrado=""
    for Caracter in Mensaje:
        if not Caracter.isalpha():
            continue
        Caracter = Caracter.upper()
        Codigo = ord(Caracter)+1
        if Codigo > ord("Z"):
            Codigo = ord("A")
        Cifrado += chr(Codigo)
    return Cifrado


