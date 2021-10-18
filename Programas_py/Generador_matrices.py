import csv
from datetime import datetime

#Variables globales .....................................

registro_de_juegos = []
top_global = []

registro_juegos_localidad = "Juego_integrador/datos/registro_de_juegos.csv"
top_global_localidad = "Juego_integrador/datos/top_global.csv"


#........................................................

#Genera matriz a partir de un archivo
#Parametro de ----->>  || archivo.csv inicio || nombre de matriz||

def cargarMatriz(archivo_de_convercion,matriz_generada):
    archivo_a_convertir = open(archivo_de_convercion)
    contenido = archivo_a_convertir.readlines()
    for line in contenido:
        matriz_generada.append(line.upper().strip().split(','))
    archivo_a_convertir.close()

#Guarda matriz modificada 
#parametro de ------>> || archivo.csv destino || matriz modificada 
def guardarMatriz(archivo_a_guardar,matriz_generada_guardar):
    string_content = ""
    for lines in matriz_generada_guardar:
        for idx, element in enumerate(lines):
            if idx == len(lines) -1:
                string_content += str(element) + '\n'
            else:
                string_content += str(element) + ','

    string_content = string_content.strip()
    archivo_productos = open (archivo_a_guardar, 'w')
    archivo_productos.write(string_content)
    archivo_productos.close()


def matriz_registro_juegos():
    cargarMatriz(registro_juegos_localidad,registro_de_juegos)
    return registro_de_juegos

def matriz_top_global():
    cargarMatriz(top_global_localidad,top_global)
    return top_global

def guardar_registro_juegos(lista_a_registro_juegos):
    registro_juegos_anadir = [lista_a_registro_juegos[0],lista_a_registro_juegos[1],datetime.now()]
    registro_de_juegos.append(registro_juegos_anadir)
    guardarMatriz(registro_juegos_localidad,registro_de_juegos)

def guardar_top_global(lista_a_top_global):
    score=0
    top_global_anadir = [lista_a_top_global,score]
    top_global.append(top_global_anadir)
    guardarMatriz(top_global_localidad,top_global)


