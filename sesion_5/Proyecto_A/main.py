import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./UI/Restaurante.ui",self)
# Llamada de metodos por evento
        self.btnProcesar.clicked.connect(self.Proceso)
        self.btnCancelar.clicked.connect(self.Cancelar)

    def LeerDatos(self):
        self.Platillo=self.txtPlatillo.text()
        self.Precio=float(self.txtPrecio.text())
        self.Cantidad=float(self.txtCantidad.text())

    def Proceso(self):
        self.LeerDatos()
        self.importePlatos=self.Precio*self.Cantidad
        
        #Postres
        self.a=0; self.b=0; self.c=0; self.d=0; self.e=0; self.f=0;
        self.totalPostres=0
        if self.chkPostre1.isChecked():
            self.a=15.00
        if self.chkPostre2.isChecked():
            self.b=10.00
        if self.chkPostre3.isChecked():
            self.c=5.00
        if self.chkPostre4.isChecked():
            self.d=25.00
        if self.chkPostre5.isChecked():
            self.e=18.00
        if self.chkPostre6.isChecked():
            self.f=12.00
        
        self.totalPostres=self.a+self.b+self.c+self.d+self.e+self.f
        self.totalConsumo=self.importePlatos+self.totalPostres

        #Comprobante --> es aqui donde se calcula el impuesto(18%)
        self.impuesto=0
        if self.rbFactura.isChecked():
            self.impuesto=self.totalConsumo*0.18
        
        #Total General
        self.totalGeneral=self.totalConsumo+self.impuesto
        
        #Imprimir
        self.txtSalida.setText("")
        self.txtSalida.append("="*20)
        self.txtSalida.append("Restaurante los Delfines")
        self.txtSalida.append("="*20)
        self.txtSalida.append("Comprobante de Pago")
        self.txtSalida.append("="*20)
        self.txtSalida.append(f'Platillo\t: {self.Platillo}')
        self.txtSalida.append(f'Precio\t: {self.Precio}')
        self.txtSalida.append(f'Cantidad\t: {self.Cantidad}')
        self.txtSalida.append("="*20)
        self.txtSalida.append(f'Consumo Platillo\t: {self.importePlatos}')
        self.txtSalida.append(f'Consumo Postres\t: {self.totalPostres}')
        self.txtSalida.append(f'Total Consumo\t: {self.totalConsumo}')
        self.txtSalida.append(f'Impuesto (18%)\t: {self.impuesto:.2f}')
        self.txtSalida.append(f'='*20)
        self.txtSalida.append(f'Total a pagar\t: {self.totalGeneral}')
        
    def Cancelar(self):
        self.txtPlatillo.setText("")
        self.txtPrecio.setText("")
        self.txtCantidad.setText("")
        self.txtSalida.setText("")
        self.chkPostre1.setChecked(False)
        self.chkPostre2.setChecked(False)
        self.chkPostre3.setChecked(False)
        self.chkPostre4.setChecked(False)
        self.chkPostre5.setChecked(False)
        self.chkPostre6.setChecked(False)
        self.rbBoleta.setChecked(1)
        self.rbFactura.setChecked(0)
        self.txtPlatillo.setFocus()
        

if __name__ == '__main__':
    app=QApplication(sys.argv)
    GUI=ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())
    
