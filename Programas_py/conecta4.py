from lib_frames_conecta4 import *
import  os
from datetime import datetime
reg_top = []
reg_juegos = []

def ingreso_de_datos(op):
    jugador_2 = "Computadora"
    jugador_1 = input("Nombre del jugador 1: ")
    if int(op) == 2:
        jugador_2 = input("Nombre del jugador 2: ")
    return (jugador_1,jugador_2)

def regreso_top(jugador_ganador):
    reg_top.append(jugador_ganador)

def regreso_registro(jugador_ganador,jugador_perdedor):
    reg_top.append(jugador_ganador,jugador_perdedor,datetime.now())

def main(op_juego):
    os.system("cls")
    rectangulo_matriz_pricipal(7,7)
    juego = True
    turno_jugador = 1
    jugadores = ingreso_de_datos(op_juego)
    while juego == True:
        os.system("cls")
        imprimir_forma()
        re_ingresar = True
        while re_ingresar == True:
            if turno_jugador == 1:
                print(f"Turno de {jugadores[0]} (Jugador 1)\n") 
                jugada = input("Elige tu opcion ---> ")
                if validacion_numero(jugada) == True:
                    jugada = int(jugada)
                    if jugada<=n_columnas and jugada>=0:
                        jugada-=1
                        agregar_ficha_matriz(jugada,ficha1)
                        turno_jugador = 2
                        re_ingresar = False
                    else:
                        print("Columna invalida")
                        re_ingresar == True
                else:
                        print("Columna invalida")
                        re_ingresar == True

            else:
                print(f"Turno de {jugadores[1]} (Jugador 2)\n")
                if op_juego ==2:  
                    jugada = input("Elige tu opcion ---> ")
                else:
                    jugada = valor_compu()
                if validacion_numero(jugada) == True:
                    jugada = int(jugada)
                    if jugada<=n_columnas and jugada>=0:
                        jugada-=1
                        agregar_ficha_matriz(jugada,ficha2)
                        turno_jugador = 1
                        re_ingresar = False
                    else:
                        print("Columna invalida")
                        re_ingresar == True
                else:
                        print("Columna invalida")
                        re_ingresar == True
            estado_ganadores = inspeccion()
            if estado_ganadores[0] == True:
                os.system("cls")
                imprimir_forma()
                print(Felicidades_jugador1[0])
                input()
                juego = False
            elif estado_ganadores[1] == True:
                os.system("cls")
                imprimir_forma()
                print(Felicidades_jugador2[0])
                input()
                juego = False



if __name__ == '__main__':
    inicio()
    input()
    os.system("cls")
    opcion_juego = menu()
    if int(opcion_juego) == 1 or opcion_juego == 2:
        main(opcion_juego)
    


#faltan los csv