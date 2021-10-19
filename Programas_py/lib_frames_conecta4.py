from conecta4 import *
import os
from random import randint

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

Felicidades_jugador1 = ["""
________________________________________________________________
            Ganador Jugador 1
________________________________________________________________

        Presiona enter para continuar
"""]

Felicidades_jugador2 = ["""
________________________________________________________________
            Ganador Jugador 2
________________________________________________________________

        Presiona enter para continuar
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
        if ficha == ficha1:
            estado_matriz[fila][columna] = 1
        elif ficha == ficha2:
            estado_matriz[fila][columna] = 2
    replay.append(estado_matriz)

#Imprecion de forma (retorno de un string de la forma actual)

def imprimir_forma():
    os.system('mode con: cols=85 lines=43')
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
    if str(caracter).isdigit():
        return True
    else:
        return False


def inspeccion():
    jugador1 = False
    jugador2 = False
    da = inspeccion_diagonal_ascendentes()
    dd = inspeccion_diagonal_descendente()
    lh = inspeccion_lineal_horizontal()
    lv = inspeccion_lineal_vertical()

    estdo_jugador1 = [da[0],dd[0],lh[0],lv[0]]
    estdo_jugador2 = [da[1],dd[1],lh[1],lv[1]]

    for x in range(len(estdo_jugador1)):
        if estdo_jugador1[x] == True:
            jugador1 = True
        elif estdo_jugador2[x] == True:
            jugador2 = True

    return [jugador1,jugador2]

def inspeccion_diagonal_ascendentes():
    jugador1 = False
    jugador2 = False
    for i in range(n_filas-3):
        comprobacion = []
        lista_diagonal_as = estado_matriz
        for j in range(n_columnas-3): 
            comprobacion = [lista_diagonal_as[i+3][j],lista_diagonal_as[i+2][j+1],lista_diagonal_as[i+1][j+2],lista_diagonal_as[i][j+3]]
            
            if comprobacion == [1,1,1,1]:
                jugador1=True
            elif comprobacion == [2,2,2,2]:
                jugador2=True
    return [jugador1,jugador2]

def inspeccion_diagonal_descendente():
    jugador1 = False
    jugador2 = False
    for i in range(n_filas-3):
        comprobacion = []
        lista_diagonal_as = estado_matriz
        for j in range(n_columnas-3): 
            comprobacion = [lista_diagonal_as[i][j+3],lista_diagonal_as[i+1][j+2],lista_diagonal_as[i+2][j+1],lista_diagonal_as[i+3][j]]
            if comprobacion == [1,1,1,1]:
                jugador1=True
            elif comprobacion == [2,2,2,2]:
                jugador2=True
    return [jugador1,jugador2]

def inspeccion_lineal_horizontal():
    jugador1 = False
    jugador2 = False
    for i in range(n_filas):
        comprobacion = []
        lista_horizontal = []
        for j in range(n_columnas):
            lista_horizontal.append(estado_matriz[i][j]) 
        for k in range(len(lista_horizontal)-3):
            comprobacion = [lista_horizontal[0+k],lista_horizontal[1+k],lista_horizontal[2+k],lista_horizontal[3+k]]
            if comprobacion == [1,1,1,1]:
                jugador1=True
            elif comprobacion == [2,2,2,2]:
                jugador2=True
    return [jugador1,jugador2]


def inspeccion_lineal_vertical():
    jugador1 = False
    jugador2 = False
    for j in range(n_columnas):
        comprobacion = []
        lista_vertical = []
        for i in range(n_filas):
            lista_vertical.append(estado_matriz[i][j]) 
        for k in range(len(lista_vertical)-3):
            comprobacion = [lista_vertical[0+k],lista_vertical[1+k],lista_vertical[2+k],lista_vertical[3+k]]
            if comprobacion == [1,1,1,1]:
                jugador1=True
            elif comprobacion == [2,2,2,2]:
                jugador2=True
    return [jugador1,jugador2]

def valor_compu():
    descicion_compu = randint(1, n_columnas)
    return descicion_compu

def reiniciar_variables():
    global estado_matriz 
    estado_matriz = []
    global rectangulo_principal 
    rectangulo_principal= []
    rectangulo_matriz_pricipal(7,7)

def imprimir_tablas(matriz_documento):
    string_renglon = ""
    for renglon in range(len(matriz_documento)):
        for dato in range(len(matriz_documento[renglon])):
            string_renglon = string_renglon + f"   {matriz_documento[renglon][dato]}\t"  
        string_renglon = string_renglon + "\n"  
    print (string_renglon)

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

def menu():
    menu_inicio = ["""

         _________________________________________________
        |    ESTAS SON TUS OPCIONES DE JUEGOOOOOOOO,      |
        |    ELIGE UNA:                                   |
        |                                                 |
        |    1. Juego contra la computadora               |
        |                                                 |
        |    2. Juega con un amig@ / familiar             |
        |                                                 |
        |    3. Consultar el top de ganadores             |
        |                                                 |    
        |    4. Registro de partidas jugadas              |
        |                                                 |
        |    5. Salir                                     |
        |_________________________________________________|

    """]
    print(menu_inicio[0])
    opciones_menu = False
    while opciones_menu == False:
        op_menu = input("  Ingresa tu opcion : ")
        if validacion_numero(op_menu) == True:
            if int(op_menu)<=5 and int(op_menu)>0:
                opciones_menu == True
                break

    return op_menu
        