from Generador_matrices import matriz_registro_progreso
import os

#Fichas de juego

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

#variables generales -------------------------------------------------------------------------

estado_matriz = []
rectangulo_principal=[]
n_filas=7
n_columnas=7

#Funciones de matriz de llenado de juego -----------------------------------------------------
# funciones:
# rectangulo_matriz_principal
# agregar_ficha_matriz
# imprimir_forma

#Generacion de matriz tamano de nm de filas y columnas (vacias)

def rectangulo_matriz_pricipal(filas,columnas):
     for i in range (columnas):
        lista_filas = []
        lista_filas_estado = []
        for j in range (filas):
            lista_filas.append(vacio)
            lista_filas_estado.append(0)
        estado_matriz.append(lista_filas_estado)
        rectangulo_principal.append(lista_filas)

#Agregado de ficha en columna y fila dada

def agregar_ficha_matriz(columna,ficha):
    if posiciones_y(columna) == -1:
        print("No se puede, pierdes turno")
    else:
        
        fila = posiciones_y(columna)
        rectangulo_principal[columna][fila] = ficha
        estado_matriz[columna][fila] = 1

#Imprecion de forma (retorno de un string de la forma actual)

def imprimir_forma():
    renglonk = ""
    for i in range(len(rectangulo_principal)):
        for k in range(len(rectangulo_principal[i][0])):
            for j in range(len(rectangulo_principal[i])):
                renglonk = renglonk + f"{rectangulo_principal[i][j][k][0]}"
            renglonk = renglonk + "\n"
    print(renglonk)

def posiciones_y(columna):
    posicion_libre = None
    for x in range(len(estado_matriz[0])):
        if estado_matriz[x][columna] == 0:
            posicion_libre = x
        else:
            posicion_libre = -1

    return posicion_libre
            


def inicio():
    os.system('mode con: cols=200 lines=49')
    mensaje_de_inicio = """
    
    Conecta 4
    
    """
    print(mensaje_de_inicio)



rectangulo_matriz_pricipal(7,7)
#print (rectangulo_principal)
print(estado_matriz)
agregar_ficha_matriz(5,ficha1)
#print(rectangulo_principal)
print(estado_matriz)
print(imprimir_forma())

