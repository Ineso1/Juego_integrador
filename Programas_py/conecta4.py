from lib_frames_conecta4 import *
import  os



def main():
    os.system("cls")
    rectangulo_matriz_pricipal(7,7)
    juego = True
    turno_jugador = 1
    while juego == True:
        
        os.system("cls")
        imprimir_forma()
        re_ingresar = True
        while re_ingresar == True:
            if turno_jugador == 1:
                print("Turno del Jugador 1\n") 
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
                print("Turno del Jugador 2\n") 
                jugada = input("Elige tu opcion ---> ")
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
    main()
    