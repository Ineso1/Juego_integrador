from Generador_matrices import matriz_registro_progreso


ficha1 = [
["    ***    "],
["  *******  "],
["  *******  "],
["    ***    "]
]
ficha2 = [
["    :::    "],
["  :::::::  "],
["  :::::::  "],
["    :::    "]
]
vacio = [
["           "],
["           "],
["           "],
["           "]
]
rectangulo_principal=[]
n_filas=7
n_columnas=7

def rectangulo_matriz_pricipal(filas,columnas):
     for i in range (columnas):
        lista_filas = []
        for j in range (filas):
            lista_filas.append("")
        rectangulo_principal.append(lista_filas)

def agregar_ficha_matriz(fila,columna,ficha):
    rectangulo_principal[columna][fila] = ficha

rectangulo_matriz_pricipal(n_filas,n_columnas)
#print (rectangulo_principal)
agregar_ficha_matriz(0,0,ficha1)
#print(rectangulo_principal)

for c in range(len(rectangulo_principal)):
    for v in range(len(rectangulo_principal[c])):
        for m in range(len(rectangulo_principal[c][v])):
            print(f"{rectangulo_principal[c][v][m]}",end="")
        print()

"""
def rectangulo(alto,ancho):
    matriz_rectangulo_vacio = [] 
    for i in range (alto):
        lista_anchos = []
        for j in range (ancho):
            lista_anchos.append(".")
        matriz_rectangulo_vacio.append(lista_anchos)
    return matriz_rectangulo_vacio

vacios = rectangulo(77,42)
#print(""*len(vacios[0]))
for c in range(len(vacios)):
    for v in range(len(vacios[c])):
        print(f"{vacios[c][v]}",end="")
    print()
#print(""*len(vacios[0]))

hj=input("cono guj")"""