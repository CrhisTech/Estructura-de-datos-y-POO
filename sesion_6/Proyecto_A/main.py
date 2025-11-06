import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

class EjemploGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/Registro_de_notas.ui",self)
        #Eventos
        self.btnAgregar.clicked.connect(self.AgregarFila)
        #self.btnQuitar.clicked.connect(self.LimpiarDatos)
        self.tbRegistro.clicked.connect(self.Seleccionar_Fila_Tabla)
        self.btnQuitar.clicked.connect(self.Quitar)
        self.btnModificar.clicked.connect(self.Modificar)
        
    #Aqui se pueden definir Contadores y Aculmuladores
    #Variables de Clase. (Variables Publicas de clase)
    Fila = -1 #No hay ninguna fil seleccionada
    def LeerDatos(self):
        self.Codigo = self.txtCodigo.text()
        self.ApeNom = self.txtApeNom.text()
        self.Asignatura = self.cboAsignatura.currentText()
        self.Eva1 = float(self.txtEC1.text())
        self.Eva2 = float(self.txtEC2.text())
        self.Eva3 = float(self.txtEC3.text())
        self.EvaF = float(self.txtEF.text())
        
        self.Promedio = round((self.Eva1*0.04) + (self.Eva2*0.12) + (self.Eva3*0.24) + (self.EvaF*0.60),0)
        if self.Promedio >= 13:
            self.Estado = "Aprobado"
        else:
            self.Estado = "Desaprobado"
    def LimpiarDatos(self):
        self.txtCodigo.setText("")
        self.txtApeNom.setText("")
        self.cboAsignatura.setCurrentIndex(0)
        self.txtEC1.setText("")
        self.txtEC2.setText("")
        self.txtEC3.setText("")
        self.txtEF.setText("")
        self.txtCodigo.setFocus()
    def AgregarFila(self):
        #.rowCount() Nos devuelve el numero de filas que tiene la tabla
        #.setRowCount(#filas) Establece el numero de filas que tendra la tabla
        #.setItem(fila, columna, dato) Establece el dato en la fila y columna indicada
        self.LeerDatos()
        indice = self.tbRegistro.rowCount()
        self.tbRegistro.setRowCount(indice + 1)
        #Agregar los datos a la tabla
        self.tbRegistro.setItem(indice,0,QTableWidgetItem(self.Codigo))
        self.tbRegistro.setItem(indice,1,QTableWidgetItem(self.ApeNom))
        self.tbRegistro.setItem(indice,2,QTableWidgetItem(self.Asignatura))
        self.tbRegistro.setItem(indice,3,QTableWidgetItem(str(self.Eva1)))
        self.tbRegistro.setItem(indice,4,QTableWidgetItem(str(self.Eva2)))
        self.tbRegistro.setItem(indice,5,QTableWidgetItem(str(self.Eva3)))
        self.tbRegistro.setItem(indice,6,QTableWidgetItem(str(self.EvaF)))
        self.tbRegistro.setItem(indice,7,QTableWidgetItem(str(self.Promedio)))
        self.tbRegistro.setItem(indice,8,QTableWidgetItem(self.Estado))
    def Seleccionar_Fila_Tabla(self):
        #.currentRow() --> Comando de la Tabla que devuelve la posicion de la fila seleccionada
        #.removeRow() --> Comando de la Tabla que remueve o elimina una fila de la Tabla 
        self.Fila = self.tbRegistro.currentRow()
        #Agregamos esto solo para Modificar una Fila
        self.txtCodigo.setText(self.tbRegistro.item(self.Fila,0).text())
        self.txtApeNom.setText(self.tbRegistro.item(self.Fila,1).text())
        self.cboAsignatura.setCurrentText(self.tbRegistro.item(self.Fila,2).text())
        self.txtEC1.setText(self.tbRegistro.item(self.Fila,3).text())
        self.txtEC2.setText(self.tbRegistro.item(self.Fila,4).text())
        self.txtEC3.setText(self.tbRegistro.item(self.Fila,5).text())
        self.txtEF.setText(self.tbRegistro.item(self.Fila,6).text())
    def Modificar(self):
        self.LeerDatos()
        #Re-Grabar con los datos modificados
        self.tbRegistro.setItem(self.Fila,0,QTableWidgetItem(self.Codigo))
        self.tbRegistro.setItem(self.Fila,1,QTableWidgetItem(self.ApeNom))
        self.tbRegistro.setItem(self.Fila,2,QTableWidgetItem(self.Asignatura))
        self.tbRegistro.setItem(self.Fila,3,QTableWidgetItem(str(self.EC1)))
        self.tbRegistro.setItem(self.Fila,4,QTableWidgetItem(str(self.EC2)))
        self.tbRegistro.setItem(self.Fila,5,QTableWidgetItem(str(self.EC3)))
        self.tbRegistro.setItem(self.Fila,6,QTableWidgetItem(str(self.EF)))
        self.tbRegistro.setItem(self.Fila,6,QTableWidgetItem(str(self.Promedio)))
        self.tbRegistro.setItem(self.Fila,6,QTableWidgetItem(str(self.Estado)))
        self.Limpiar()
        
    def Quitar(self):
        if self.Fila == -1: # --> En caso no se ha seleccionado alguna fila, se muestra el siguiente mensaje:
            print("Error: No se ha seleccionado ninguna Fila")
        else:
            self.tbRegistro.removeRow(self.Fila)
            self.Fila=-1 # --> Obliga al usuario a marcar una fila para eliminar
            print("Fila de datos Eliminada con Exito")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = EjemploGUI()
    GUI.show()
    sys.exit(app.exec_())