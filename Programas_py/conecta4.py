from Generador_matrices import *
from lib_frames_conecta4 import *
import  os
from datetime import datetime

#::::::::::::::::::::::::::::

registro_de_juegos = []
top_global = []

#::::::::::::::::::::::::::::

def cargar_archivos():
    cargarMatriz(registro_juegos_localidad,registro_de_juegos)
    cargarMatriz(top_global_localidad,top_global)


def registro_datos_partida(jugador_ganador,jugador_perdedor):
    score=0

    lista_a_registro_juegos = [jugador_ganador,jugador_perdedor]
    lista_a_top_global = jugador_ganador
    registro_juegos_anadir = [lista_a_registro_juegos[0],lista_a_registro_juegos[1],datetime.now()]
    registro_de_juegos.append(registro_juegos_anadir)
    guardarMatriz(registro_juegos_localidad,registro_de_juegos)
    top_global_anadir = [lista_a_top_global,score]
    top_global.append(top_global_anadir)
    guardarMatriz(top_global_localidad,top_global)

    print("Partida guardada")
    input()


def ingreso_de_datos(op):
    jugador_2 = "Computadora"
    jugador_1 = input("Nombre del jugador 1: ")
    if int(op) == 2:
        jugador_2 = input("Nombre del jugador 2: ")
    return (jugador_1,jugador_2)
"""
def regreso_top(jugador_ganador):
    reg_top.append(jugador_ganador)

def regreso_registro(jugador_ganador,jugador_perdedor):
    reg_top.append([jugador_ganador,jugador_perdedor,datetime.now()])
    guardar_registro_juegos(reg_top)
"""

def main(op_juego):
    os.system("cls")
    reiniciar_variables()
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
                if int(op_juego) == 2:  
                    jugada = input("Elige tu opcion ---> ")
                else:
                    jugada = valor_compu()
                    input("Enter para continuar")
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
                registro_datos_partida(jugadores[0],jugadores[1])
                input()
                juego = False
            elif estado_ganadores[1] == True:
                os.system("cls")
                imprimir_forma()
                print(Felicidades_jugador2[0])
                registro_datos_partida(jugadores[1],jugadores[0])
                input()
                juego = False
                
    os.system("cls")


if __name__ == '__main__':
    cargar_archivos()
    inicio()
    input()
    opcion_juego = 1
    os.system("cls")
    opcion_juego = menu() 
    while opcion_juego != "5":
        os.system("cls")
        if opcion_juego == "1" or opcion_juego == "2":
            main(opcion_juego)
        elif opcion_juego == "3":
            os.system("cls")
            print("""
    Jugador || Numero de partidas ganadas
    """)
            imprimir_tablas(top_global)
            input("\n  Preciona ENTER para continuar")
        elif  opcion_juego == "4":
            os.system("cls")
            print("""
    Ganador  || Perdedor  || Fecha
    """)
            imprimir_tablas(registro_de_juegos)
            input("\n  Preciona ENTER para continuar")
        else:
            os.system("cls")
            print("Valor no valido en el menu\n")
            opcion_juego = menu()
        os.system("cls")
        opcion_juego = menu() 
    

