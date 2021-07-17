#Nombre: Lady Mishell Gauin Gusñay
# 3cer Semestre Ing. en Software A1
# ejercicio en clase 2021-06-11

class ciclo:
    
    def __init__(self,numero=5):
        self.numero=numero
        self.numero2=0
    
    def usoWhile(self):
        # ciclo repetitivo que se ejecuta mientras la condicion se cumple(verdadero),
        #es decir solo por falso
        car = input("Ingrese vocal: ")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car = input("Ingrese vocal: ").lower()
        print("Felicitación su vocal es: {}".format(car))
            
ciclo1 = ciclo()
ciclo1.usoWhile()
print("fin de uso ciclo")     