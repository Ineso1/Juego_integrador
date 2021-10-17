from lib_frames_conecta4 import *
import  os


def main():
    os.system("cls")
    rectangulo_matriz_pricipal(7,7)
    imprimir_forma()
    juego = True
    while juego == True:
        turno_jugador = 1
        if turno_jugador == 1: 
            jugada = input("---> ")
            agregar_ficha_matriz(jugada,ficha1)
            turno_jugador = 2
        else:
            jugada = input("---> ")
            agregar_ficha_matriz(jugada,ficha2)
            turno_jugador = 1
        imprimir_forma()


if __name__ == '__main__':
    inicio()
    main()