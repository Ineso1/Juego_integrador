import Generador_matrices
import juego1
import juego2
import juego3
import juego4
import lib_frames
import os
import datetime

topGlobal= Generador_matrices.matriz_top_global()
registroProgreso = Generador_matrices.matriz_registro_progreso()

def main():
    print(f"""
    {topGlobal}
    {registroProgreso}
    """)
    topGlobal.append(["Ines Alejandro",500000])
    registroProgreso.append(["Ines Alejandro",500000,datetime.datetime.now()])


if __name__=='__main__':
    main()
    Generador_matrices.guardar_registro_progreso(registroProgreso)
    Generador_matrices.guardar_top_global(topGlobal)
