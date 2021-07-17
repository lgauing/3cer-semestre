#Nombre: Lady Mishell Gauin Gusñay
# 3cer Semestre Ing. en Software A1
#ejercicio en clase 2021-06-11

class condición():
    
    def __init__(self, num1=5,num2=4):
        self.numero1=num1
        self.numero2=num2
        numero=self.numero1+self.numero2
        self.numero3=numero
    
    def usoIf(self):
        # if...elif....else..:permiten condicionar la ejcucion de uno o varios bloques de codigos
        # de sentencias al cumplimiento de una o varias condiones.
        
        if self.numero1 == self.numero2:
            print("numero1={}, numero2={}: son iguales".format(self.numero1, self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1 y numero3 son iguales")
        else:
            print("numeros diferentes")     
        print("fin if")    
            
        # print(self.numero3)
        
# print("instancia de la clase")
cond1=condición(10,10)  
# cond2=condición()
# print(cond2.numero3)      
cond1.usoIf()
# cond2.usoIf()
print("Gracias por su visita")