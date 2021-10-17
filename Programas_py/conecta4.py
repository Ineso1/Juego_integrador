from lib_frames_conecta4 import *
import  os


def main():
    os.system("cls")
    rectangulo_matriz_pricipal(7,7)
    juego = True
    while juego == True:
        imprimir_forma()
        turno_jugador = 1
        if turno_jugador == 1: 
            os.system("cls")
            jugada = int(input("---> "))
            agregar_ficha_matriz(jugada,ficha1)
            turno_jugador = 2
        else:
            os.system("cls")
            jugada = int(input("---> "))
            agregar_ficha_matriz(jugada,ficha2)
            turno_jugador = 1


if __name__ == '__main__':
    inicio()
    main()