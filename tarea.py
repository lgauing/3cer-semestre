#Nombre: Lady Mishell Gauin Gusñay
# 3cer Semestre Ing. en Software A1
#ejercicio en clase 2021-06-25

class Tarea:
    def __init__(self):
        pass
    def CalcularJornada(self):
         ht, he, het=0,0,0
         ph, phe,pt,ph8=0,0,0,0
         ht=int(input("Ingrese horas trabajadas : "))
         ph=float(input("ingrese valor hora : "))
         if ht > 40:
             he=ht-40
             if he>8:
                het=he-8
                ph8= 8*ph*2
                phe= het*ph*3
             else:
                 phe=0
                 ph8=he*ph*2
             pt=40*ph+ph8+phe  
         else:
             pt=ht*ph    
         print("sobretiempo<8: {} Sobretiempo>8: {} jornada : {} ".format(ph8,phe,pt))
tarea=Tarea()
tarea.CalcularJornada()         