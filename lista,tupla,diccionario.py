#Nombre: Lady Mishell Gauin Gusñay
# 3cer Semestre Ing. en Software A1
# Guia dispositiva

# Tuplas – Listas - Diccionarios
usuario = ("Lgauin", "146", "Ladygauin-123@hotmail.com")
materias = ["Estructura_de_datos", "ecuaciones", "modelamiento_de_Software"]
docente = {"nombre":"Lady", "edad":23,"fac":"faci"}
print(usuario[0],materias[1],docente["nombre"])
print(usuario[0:2],docente.keys(),docente.values())
tupla,lista,diccionario=(),[],{}

materias.append("Estructura_de_datos")
docente["sexo"], docente["edad"]="Femenino", 23
print(materias,docente)
tupla,lista,diccionario=(),[],{}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,':',c)
# Recorridos diccionario con items
for c, v in docente.items(): print(c,':',v)