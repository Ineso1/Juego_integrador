import csv

#Variables globales .....................................

registro_progreso = []
top_global = []

registro_progreso_localidad = "Juego_integrador/datos/registro_progresos.csv"
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


def matriz_registro_progreso():
    cargarMatriz(registro_progreso_localidad,registro_progreso)
    return registro_progreso

def matriz_top_global():
    cargarMatriz(top_global_localidad,top_global)
    return top_global

def guardar_registro_progreso(matriz_modificada_registro_progreso):
    registro_progreso = matriz_modificada_registro_progreso
    guardarMatriz(registro_progreso_localidad,registro_progreso)

def guardar_top_global(matriz_modificada_top_global):
    top_global = matriz_modificada_top_global
    guardarMatriz(top_global_localidad,top_global)

