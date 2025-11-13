class Alumno():
    #1. Atributos:
    Codigo=0; ApeNom=""; Asignatura=""; Eva1=0;
    Eva2=0; Eva3=0; EvaF=0
    
    #2. Constructor:
    def __init__(self, codigo, apenom, asignatura, ec1, ec2, ec3, ef):
        self.Codigo = codigo
        self.ApeNom = apenom
        self.Asignatura = asignatura
        self.Eva1 = ec1
        self.Eva2 = ec2
        self.Eva3 = ec3
        self.EvaF = ef
    
    
    #3. Metodos y Operaciones:
    def Promedio(self):
        prom = (self.Eva1*0.04) + (self.Eva2*0.12) + (self.Eva3*0.24) + (self.EvaF*0.6)
        return prom
    
    def Estado(self):
        est=""
        if self.Promedio() >= 13:
            est="Aprobado"
        else:
            est = "Desaprobado"
        return est
    
    def NotaMayor(self):
        notas=[self.Eva1,self.Eva2,self.Eva3,self.EvaF,]
        return max(notas)
    
    def NotaMenor(self):
        notas=[self.Eva1,self.Eva2,self.Eva3,self.EvaF,]
        return min(notas)
        