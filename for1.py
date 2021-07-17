#Nombre: Lady Mishell Gauin Gusñay
# 3cer Semestre Ing. en Software A1
# Guia dispositiva

# for range(v) – range(vi,vf)  - range(vi,vf,inc)
frase = input("Ingrese frase: ")
cvoc=0
# for in cadena - in(tupla) – in[lista]  
for indice in range(len(frase)):
    print(indice,'=',frase[indice])
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
print('cantidad vocales:{}'.format(cvoc))
# Comprehension – [var for var in datos condicion]
[car for car in['a','e','i','o','u'] if car not in('a','i','o')]