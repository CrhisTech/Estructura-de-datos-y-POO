import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

#Importando la clase Alumno() del archivo alumno.py
from Controlador.alumno import Alumno

#Crear el Objeto "Estudiante" de tipo Clase Alumno
Estudiante=Alumno(0,'','',0,0,0,0)

class ejemploGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/Registro_de_Notas.ui",self)
        
        #Eventos
        self.btnProcesar.clicked.connect(self.Procesar)
        self.btnCancelar.clicked.connect(self.LimpiarControles)

    # Llamada de metodos por evento
    def LeerDatos(self):
        Estudiante.Codigo=str(self.txtCodigo.text())
        Estudiante.ApeNom=(self.txtApeNom.text())
        Estudiante.Asignatura=(self.cboAsignatura.currentText())
        Estudiante.Eva1=int(self.txtEC1.text())
        Estudiante.Eva2=int(self.txtEC2.text())
        Estudiante.Eva3=int(self.txtEC3.text())
        Estudiante.EvaF=int(self.txtEF.text())

    def Imprimir(self, ObjectClase):
        self.txtSalida.setText("")
        self.txtSalida.append("="*30)
        self.txtSalida.append("Datos del Estudiante")
        # Unir en una sola cadena en cada append
        self.txtSalida.append(f"Codigo\t: {ObjectClase.Codigo}")
        self.txtSalida.append(f"Apellidos y Nombres: {ObjectClase.ApeNom}")
        self.txtSalida.append(f"Asignatura\t: {ObjectClase.Asignatura}")
        self.txtSalida.append("="*30)
        self.txtSalida.append("Calificaciones")
        self.txtSalida.append("="*30)
        self.txtSalida.append(f"Evaluacion continua 1\t: {ObjectClase.Eva1}")
        self.txtSalida.append(f"Evaluacion continua 2\t: {ObjectClase.Eva2}")
        self.txtSalida.append(f"Evaluacion continua 3\t: {ObjectClase.Eva3}")
        self.txtSalida.append(f"Evaluacion Final\t: {ObjectClase.EvaF}")
        self.txtSalida.append("="*30)
        self.txtSalida.append(f"Promedio\t: {ObjectClase.Promedio()}")
        self.txtSalida.append(f"Estado\t: {ObjectClase.Estado()}")
        self.txtSalida.append(f"Nota Mayor: {ObjectClase.NotaMayor()}")
        self.txtSalida.append(f"Nota Menor: {ObjectClase.NotaMenor()}")
        self.txtSalida.append("")

    def Procesar(self):
        self.LeerDatos()
        self.Imprimir(Estudiante)
        self.LimpiarControles()

    def LimpiarControles(self):
        self.txtCodigo.setText("")
        self.txtApeNom.setText("")
        self.cboAsignatura.setCurrentIndex(0)
        self.txtEC1.setText("")
        self.txtEC2.setText("")
        self.txtEC3.setText("")
        self.txtEF.setText("")
        self.txtCodigo.setFocus()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemploGUI()
    GUI.show()
    sys.exit(app.exec_())