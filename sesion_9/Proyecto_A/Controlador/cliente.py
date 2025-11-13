#Clases Colaborativas

class Cliente():
    #1. Atributos:
    Nombre=""; Monto=0.0

    #2. Constructor
    def __init__(self, nombre):
        self.Nombre=nombre
        self.Monto=0.0

    #3. Metodos y Operaciones:
    def Depositar(self, monto):
        self.Monto=self.Monto+monto
    
    def Extraer(self, monto):
        self.Monto=self.Monto-monto
    
    def ConsultarMonto(self):
        return self.Monto

    def Imprimir(self):
        print(self.Nombre, "Tiene depositado la suma de:", self.Monto)

class Banco():
    #1. Atributos:

    #2. Constructor:
    def __init__(self):
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Carlos")
        self.cliente3 = Cliente("Alberto")

    def Operar(self):
        self.cliente1.Depositar(100)
        self.cliente2.Depositar(200)
        self.cliente3.Depositar(300)
        self.cliente3.Extraer(150)

    def Deposito_Totales(self):
        Total = self.cliente1.ConsultarMonto() + self.cliente2.ConsultarMonto() + self.cliente3.ConsultarMonto()
        print("El total del dinero en el Banco es:", Total)
        self.cliente1.Imprimir()
        self.cliente2.Imprimir()
        self.cliente3.Imprimir()

# Programa principal
banco=Banco()

banco.Operar()
banco.Deposito_Totales()