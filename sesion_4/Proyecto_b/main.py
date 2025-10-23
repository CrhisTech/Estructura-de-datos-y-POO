import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/Restaurante.ui', self)
# Llamada de metodos por evento
        self.btnProcesar.clicked.connect(self.Procesar)
        self.btnNuevo.clicked.connect(self.Limpiar)

    def Lectura_Datos(self):
        self.Plato = self.txtPlatillo.text()
        self.Precio = float(self.txtPrecio.text())
        self.Cantidad = float(self.txtCantidad.text())

    def Procesar(self):
         self.Lectura_Datos()
         self.Importe = self.Precio * self.Cantidad
         self.Impuesto = self.Importe * 0.18
         self.Total = self.Importe + self.Impuesto

        #Imprimir
         self.txtSalida.setText("")
         self.txtSalida.append("="*20)
         self.txtSalida.append("  Comprobante de Pago  ")
         self.txtSalida.append("="*20)
         self.txtSalida.append(f'Platillo\t: {self.Plato}')
         self.txtSalida.append(f'Precio\t: {self.Precio}')
         self.txtSalida.append(f'Cantidad\t: {self.Cantidad}')
         self.txtSalida.append("="*20)
         self.txtSalida.append(f'Importe\t: {self.Importe}')
         self.txtSalida.append(f'IGV(18%)\t: {self.Impuesto:.2f}')
         self.txtSalida.append(f'Total\t: {self.Total}')
        
    def Limpiar(self):
         self.txtPlatillo.setText("")
         self.txtPrecio.setText("")
         self.txtCantidad.setText("")
         self.txtSalida.setText("")
         self.txtPlatillo.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())


