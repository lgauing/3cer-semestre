#Nombre: Lady Mishell Gauin Gusñay
# 3cer Semestre Ing. en Software A1
# Guia dispositiva

#uso de while infinito 
s = 1
while True:
    print(s)
    break
# while validacion
vocal = input("Ingrese vocal:")
while vocal not in('a','e','i','o','u'):
    if vocal == '.':
        break
    vocal = input("Igrese nuevamente una vocal:")
print('Su vocal o punto es: {}'.format(vocal))