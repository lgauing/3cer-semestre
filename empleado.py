#Nombre: Lady Mishell Gauin Gusñay
# 3cer Semestre Ing. en Software A1
#Ejercicios en clase con el docente 21/06/2021

from cargo2 import Cargo

class Empleado:
    secuencia=0
    def __init__(self,nom="",sue=0, car=None):
        # Empleado.secuencia=Empleado.secuencia+1
        # self.codigo=Empleado.secuencia
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.sueldo=sue
        self.cargoEmp=car
        
    def generarCodigo(self):
         Empleado.secuencia=Empleado.secuencia+1
         return Empleado.secuencia
     
    def mostrar(self):
         print("codigo;{} Nombre:{} Cargo({}):{}".format(self.codigo,self.nombre,self.cargoEmp.codigo,self.cargoEmp.descripcion))

cargo1= Cargo("Docente")
emp1= Empleado("Nicole",200,cargo1)
emp1.mostrar()
emp2= Empleado("Angela",300,cargo1)
emp2.mostrar()