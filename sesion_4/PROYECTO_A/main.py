import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/Restaurante.ui",self)

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
    
    # Imprimir
        self.txtSalida.setText("")
        self.txtSalida.append("=====================")
        self.txtSalida.append("  Comprobante de Pago  ")
        self.txtSalida.append("=====================")
        self.txtSalida.append("Platillo\t: " +self.Plato)
        self.txtSalida.append("Precio\t: " +str(self.Precio))
        self.txtSalida.append("Cantidad\t: " +str(self.Cantidad))
        self.txtSalida.append("=====================")
        self.txtSalida.append("Importe\t: " +str(self.Importe))
        self.txtSalida.append("IGV(18%)\t:{:.2f}".format(self.Impuesto))
        self.txtSalida.append("Total\t: " +str(self.Total))
    
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
