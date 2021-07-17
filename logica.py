#Nombre: Lady Mishell Gauin Gusñay
# 3cer Semestre Ing. en Software A1
# ejercicio en clase 2021-07-12

class Ejercicios:
    # def __init__(self, datos):
    #     self.valor=datos
    def __init__(self):
        pass
    
    def parImpar(self,numero):
        if numero % 2 == 0: 
            print("{} es par".format(numero))
        else:
            print("{} es impar".format(numero))
    
    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+i 
        if numero == acu:
                print("{} es perfecto".format(numero))
        else:
            print("{} no es perfecto".format(numero))           
    
    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+i
        return acu            
    
ejer= Ejercicios()
# num=int(input("ingrese un numero: "))
# print("llamada 1")
# resp=ejer.perfecto2(num)
# if num == resp:
#     print("{} es perfecto".format(num))
# else:
#     print("{} No es perfecto".format(num))   
# # input()

# ejer.perfecto(num)
# input()
# lista = [2,3,1,5,6,8,10]
# print("llamada 2")
# for num in lista:
#     ejer.parImpar(num)      
# input()
# print("llamada 3")
# ejer.parImpar(23)

# lista = [3,5,6,8,28]
# print("llamada 2")
# for num in lista:
#     ejer.perfecto(num)      
# input()
# print("llamada 3")
# ejer.perfecto(23)

lista = [3,5,6,8,28]
print("llamada 2")
perfectos=[]
for num in lista:
    if ejer.perfecto2(num) == num:
        perfectos.append(num)
print(perfectos)         