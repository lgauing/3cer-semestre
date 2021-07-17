#Nombre: Lady Mishell Gauin Gusñay
# 3cer Semestre Ing. en Software A1
#ejercicio en clase 2021-06-14

class For:
    
    def __init__(self):
        pass 
    
    def usoFor(self):
        # ciclo repetitivo de incrementos o decrementos se ejecuta por verdadera
        nombre="Lady"
        datos=["Lady", 23, True]
        numeros=(2,5,6,4,1)
        docente = {'nombre':'Lady','edad':23,'fac':'faci'}
        listaNotas=[(30,40),(20,40),(50,40)]
        listaAlumnos= [{"nombre":"Lady", "final":70},{"nombre":"Stefany", "final":60},{"nombre":"Nicky","final":90}]
        
        # range[(inicio=0)], limite, [inc/dec=1].Genera un rango de valores desde un valor inicial
        # se ejecuta desde inicio hasta el limite
        # for con range() o for con colecciones
        
        # j=0
        # while j<5:
        #     print('while',j)
        #     j=j+1
        
        # for i in range(5): # rango(0,1,2,3,4)
        #     print('for',i, end=" ")
        # print()    
        # for i in range(1,5): # rango(1,2,3,4)
        #     print('for',i, end=" ")    
        # print()     
        # for i in range(2,10,2): # rango(2,4,6,8)
        #     print('for',i, end=" ")  
        # print()     
        # for i in range(12,3,-3): # rango(12,9,8)
        #     print('for',i, end=" ")
            
        # lon = len(nombre)
        # for pos in range(lon):
        #     if pos%2 == 0 and pos!=0:
        #      print(pos,nombre[pos])
        
        #   vocal = ('a','e','i','o','u')
        #   for elem in datos:
        #       print(elem, end=" ")            
        # for elem in nombre:
        #     print(elem,end=" ")
        
        # lon = len(datos)
        # for pos in range(lon):
        #     print(pos,datos[pos])
        
        # for pos, valor in enumerate(datos):
        #     print(pos,valor)
        
        # for clave, valor in docente.items():
        #     print(clave,valor,end=" ")
        
        # for notas in listaNotas:
        #     for nota in notas:
        #         print(nota, end=" ")
        
        # print(listaNotas)
        # for notas in listaNotas:
        #     print("for extremo", notas)
        #     for nota in notas:
        #         print(nota,end=" ")
        #     print("saliendo del for interno") 
        
        print(listaNotas)
        for notas in listaNotas:
            acum=0
            for nota in notas:
                acum=acum+nota
            print(acum/len(notas),end=" ")
        
        # print("\nDiccionario de notas")
        # for alumnos in listaAlumnos:
        #     for clave, valor, in alumnos.items():
        #         print(clave,":", valor,end=" ")
        #     print()    
             
bucle = For()
bucle.usoFor()