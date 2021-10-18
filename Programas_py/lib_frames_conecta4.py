from Generador_matrices import matriz_registro_progreso
import os

#Fichas de juego

ficha1 = [
["    ooo    "],
["  ooooooo  "],
["  ooooooo  "],
["    ooo    "]
]
ficha2 = [
["    xxx    "],
["  x:::::x  "],
["  x:::::x  "],
["    xxx    "]
]
vacio = [
["     .     "],
["     .     "],
["     .     "],
["     .     "]
]

renglon_inferior = ["""
__________ __________ __________ __________ __________ __________ __________
     ^          ^          ^          ^          ^          ^          ^
     1          2          3          4          5          6          7

"""]

#variables generales -------------------------------------------------------------------------

replay = []
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
    if len(posiciones_y(columna)) == 0:
        print("No se puede, pierdes turno")
    else:
        
        fila = max(posiciones_y(columna))
        rectangulo_principal[fila][columna] = ficha
        estado_matriz[fila][columna] = 1
    replay.append(estado_matriz)

#Imprecion de forma (retorno de un string de la forma actual)

def imprimir_forma():
    os.system('mode con: cols=85 lines=49')
    renglonk = ""
    for i in range(len(rectangulo_principal)):
        for k in range(len(rectangulo_principal[i][0])):
            for j in range(len(rectangulo_principal[i])):
                renglonk = renglonk + f"{rectangulo_principal[i][j][k][0]}"
            renglonk = renglonk + "\n"
    print(renglonk)
    print(renglon_inferior[0])

def posiciones_y(columna):
    posicion_libre = []
    for x in range(len(estado_matriz[0])):
        if estado_matriz[x][columna] == 0:
            posicion_libre.append(x)

    return posicion_libre
            
def validacion_numero(caracter):
    if caracter.isdigit():
        return True
    else:
        return False

def inicio():
    os.system('mode con: cols=80 lines=20')
    mensaje_de_inicio = """

                             Bienvenido a Conecta 4
        _______   ______    ___  __   ______  _______  ________    __   __
       /  ____/  / ___  /  /  | / /  /:::::/ /  ____/ /__   __/   / /__/ /
      /  /___   / /__/ /  /   |/ /  /:/:/   /  /___     /  /     /___   _/
     /______/  /______/  /__/|__/  /:::::/ /______/    /__/         /__/  




                          Presiona enter para comenzar 


    """
    print(mensaje_de_inicio)


"""
rectangulo_matriz_pricipal(7,7)
#print (rectangulo_principal)
print(estado_matriz)
agregar_ficha_matriz(5,ficha1)
#print(rectangulo_principal)
print(estado_matriz)
print(imprimir_forma())

"""

