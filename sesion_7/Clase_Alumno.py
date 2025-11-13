# Clases y Objetos
#Forma 1:

class Alumno():
    #1 Atributos o Caracteristicas.
    Codigo=0; Nombre=""; Asignatura="";
    Nota1=0.0; Nota2=0.0; Nota3=0.0; Nota4=0.0
    
    #2 Constructor (Por ahora no es necesario)
    
    #3 Metodos & Operaciones
    def Promedio(self):
        p=(self.Nota1*0.04)+(self.Nota2*0.12)+(self.Nota3*0.24)+(self.Nota4*0.6)
        return p
    
    def Estado(self):
        Est=""
        if self.Promedio() >= 13:
            Est="Aprobado"
        else:
            Est="Desaprobado"
        return Est
            
    def NotaMayor(self):
        Notas=[self.Nota1, self.Nota2, self.Nota3, self.Nota4]
        return max(Notas)
    
    def NotaMenor(self):
        Notas=[self.Nota1, self.Nota2, self.Nota3, self.Nota4]
        return min(Notas)
    
    def Imprimir(self):
        print("="*30)
        print("Detalle de Calificaciones")
        print("="*30)
        print("Codigo\t:", self.Codigo)
        print("Nombre\t:", self.Nombre)
        print("Asignatura\t:", self.Asignatura)
        print("Calificacion 1\t:", self.Nota1)
        print("Calificacion 2\t:", self.Nota2)
        print("Calificacion 3\t:", self.Nota3)
        print("Calificacion 4\t:", self.Nota4)
        print("="*30)
        print(f"Promedio\t: {self.Promedio():.2f}")
        print("Estado\t:", self.Estado())
        print("Nota Mayor\t:", self.NotaMayor())
        print("Nota Menor\t:", self.NotaMenor())
        print("="*30)
#Programa Principal (Es el que realiza la llamada de la clase)

#Ejemplo 1: Crear el objeto "Carlos" el cual representa a la clase "Alumno"
#Esta clase sera alimentada por los siguientes datos:
#Codigo=1000, Nombre="Carlos Rojas Peralta" 
#Asignatura="Ingles", Nota1=16, Nota2=15, Nota3=17, Nota4= 18

Carlos=Alumno()
Carlos.Codigo=1000
Carlos.Nombre="Carlos Rojas Peralta"
Carlos.Asignatura="Ingles"
Carlos.Nota1=16
Carlos.Nota2=17
Carlos.Nota3=18
Carlos.Nota4=15
Carlos.Imprimir()


#Ejemplo 2: Crear el objeto "Crhistopher" el cual representa a la clase "Alumno"
#Esta clase sera alimentada por los siguientes datos:
#Codigo=1001, Nombre="Crhistopher Capcha Gamarra" 
#Asignatura="Base de Datos", Nota1=18, Nota2=15, Nota3=17, Nota4= 20

Crhistopher=Alumno()
Crhistopher.Codigo=1001
Crhistopher.Nombre="Crhistopher Capcha Gamarra"
Crhistopher.Asignatura="Base de Datos"
Crhistopher.Nota1=18
Crhistopher.Nota2=15
Crhistopher.Nota3=17
Crhistopher.Nota4=20
Crhistopher.Imprimir()

#Ejemplo 3: Crear el objeto "Alberto" el cual representa a la clase "Alumno"
#Esta clase sera alimentada por los siguientes datos:
#Codigo=1002, Nombre="Alberto Perales Mazza" 
#Asignatura="Programacion Orientada a Objetos", Nota1=15, Nota2=14, Nota3=17, Nota4= 10

Alberto=Alumno()
Alberto.Codigo=1002
Alberto.Nombre="Alberto Perales Mazza"
Alberto.Asignatura="Programacion Orientada a Objetos"
Alberto.Nota1=15
Alberto.Nota2=14
Alberto.Nota3=17
Alberto.Nota4=10
Alberto.Imprimir()

#Ejemplo 3: Crear el objeto "Alberto" el cual representa a la clase "Alumno"
#Esta clase sera alimentada por los siguientes datos:
#Codigo=1002, Nombre="Alberto Salas Valdeon" 
#Asignatura="Programacion Orientada a Objetos", Nota1=16, Nota2=20, Nota3=17, Nota4= 10

print("Cambiando Nombres a Alberto")
Alberto.Nombre="Alberto Salas Valdeon"
Alberto.Nota1=16
Alberto.Nota2=20
Alberto.Nota3=17
Alberto.Nota4=10
Alberto.Imprimir()