class Comprobante():
    #1. Atributos:
    Nro=0; Nombre=""; Descripcion=""; Precio=0.0; Cantidad=0
    #2. Constructor:
    def __init__(self, nro, nombre, descripcion, precio, cantidad):
        self.Nro=nro
        self.Nombre=nombre
        self.Descripcion=descripcion
        self.Precio=precio
        self.Cantidad=cantidad
    
    #3. Metodos y Operaciones:
    def Importe(self):
        imp= self.Precio*self.Cantidad
        return imp
    
    def Igv(self):
        igv= self.Importe() * 0.18
        return igv
    
    def Total(self):
        total = self.Importe() + self.Igv()
        return  total

    def Imprimir(self):
        print("="*30)
        print(f"Comprobante de Pago Nro {self.Nro}")
        print("="*30)
        print(f"Producto:    {self.Nombre}")
        print(f"Descripcion: {self.Descripcion}")
        print(f"Precio:   {self.Precio}")
        print(f"Cantidad: {self.Cantidad}")
        print(f"Importe: {self.Importe()}")
        print(f"Igv:     {self.Igv():.2f}")
        print(f"Total:   {self.Total():.2f}")

n = input("Ingresa el nombre del producto: ")
d = input("Ingresa una breve descripcion del producto: ")
p = float(input("Ingresa el precio del producto: "))
c = int(input("Ingresa la cantidad: "))

comprobante1 = Comprobante(1, n, d, p, c)
comprobante1.Imprimir()