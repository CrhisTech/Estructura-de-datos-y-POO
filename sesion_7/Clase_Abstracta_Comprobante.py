class Comprobante():
    def __init__(self, nro, nombre, descripcion, precio, cantidad):
        self.Nro=nro
        self.Nombre=nombre
        self.Descripcion=descripcion
        self.Precio=precio
        self.Cantidad=cantidad
    
    def Importe(self):
        return self.Precio*self.Cantidad
    
    def Igv(self):
        return self.Importe()*0.18
    
    def Total(self):
        return self.Importe()+self.Igv()
    
    def Imprimir(self):
        print("="*30)
        print("Comprobante de Pago")
        print("="*30)
        print("Nro\t:", self.Nro)
        print("Cliente\t:", self.Nombre)
        print("Descipcion\t:", self.Descripcion)
        print("Precio\t: S/.", self.Precio)
        print("Cantidad\t:", self.Cantidad)
        print("="*30)
        print("Importe\t: S/", self.Importe())
        print("Igv\t: S/.", self.Igv())
        print("Total a Pagar\t: S/.", self.Total())
        print("="*30)
        
# Programa Principal (Asignar atributos a la clase Comprobante)

#Ejemplo 1: Crear el objeto "Elizabeth" el cliente de la tienda, realiza una compra
#bajo comprobante de pago del siguiente producto:
#Comprobante Nro= 1000, Nombre="Elizabeth Ramos Salas", Descripcion="SmartTV de 65p"
#Precio=S/.5600.00, Cantidad= 5. Imprimir el Comprobante

Elizabeth = Comprobante(1000, "Elizabeth Ramos Salas", "SmartTV de 65p", 5600, 5)
Elizabeth.Imprimir()


