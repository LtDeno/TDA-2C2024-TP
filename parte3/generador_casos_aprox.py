"""
Este programa es utilizado para generar instancias I de problemas de Batalla Naval Individual, los cuales luego son resueltos por un algoritmo optimo z y los algoritmo A
de aproximación (John Jellicoe y Aproximación Greedy). En el proceso, se guardan los problemas que tienen un A(I)/z(I) más chico que uno supuesto.
"""
from random import seed

import numpy as np

from parte3 import calcular_demanda_cumplida
from bt import backtracking
from jj import johnjellicoe
from ap import aproximacion


seed(12345)
np.random.seed(12345)

CASOS_A_GENERAR = 10
CANT_FILAS = 15
CANT_COLUMNAS = 15
CANT_BARCOS = 15
MAYOR_COTA_MIN_DESCUBIERTA_JJ = 0.5
MAYOR_COTA_MIN_DESCUBIERTA_AP = 0.87


def ifilas_jcolumnas_nbarcos(i, j, n):
    tablero = [[0 for _ in range(j)] for _ in range(i)]
    barcos = list(np.random.randint(1, max(i,j), n))
    d_filas = list(np.random.randint(0, j, i))
    d_columnas = list(np.random.randint(0, i, j))
    return [tablero, barcos, d_filas, d_columnas]

casos_de_prueba = []

for i in range(CASOS_A_GENERAR):
    casos_de_prueba.append(ifilas_jcolumnas_nbarcos(CANT_FILAS, CANT_COLUMNAS, CANT_BARCOS))

with open(f"jj_posibles_cotas_empiricas_gen.txt", "w") as archivo_resultados_JJ, open(f"ap_posibles_cotas_empiricas_gen.txt", "w") as archivo_resultados_AP:
    for i in range(CASOS_A_GENERAR):
        res_OPT = calcular_demanda_cumplida(backtracking(casos_de_prueba[i][0], casos_de_prueba[i][1], casos_de_prueba[i][2], casos_de_prueba[i][3]))
        res_JJ = calcular_demanda_cumplida(johnjellicoe(casos_de_prueba[i][0], casos_de_prueba[i][1], casos_de_prueba[i][2], casos_de_prueba[i][3]))
        res_APROX = calcular_demanda_cumplida(aproximacion(casos_de_prueba[i][0], casos_de_prueba[i][1], casos_de_prueba[i][2], casos_de_prueba[i][3]))
        if res_OPT == 0:
            print("OPT dió 0, no se puede poner ningún barco en este caso")
            continue
        if ((res_JJ/res_OPT) <= MAYOR_COTA_MIN_DESCUBIERTA_JJ) or ((res_APROX/res_OPT) <= MAYOR_COTA_MIN_DESCUBIERTA_AP):
            nombre_archivo_caso = f"{len(casos_de_prueba[i][2])}_{len(casos_de_prueba[i][3])}_{len(casos_de_prueba[i][1])}_caso{i}.txt"
            with open(nombre_archivo_caso, "w") as archivo_caso:
                for d_fil in casos_de_prueba[i][2]:
                    archivo_caso.write(f"{d_fil}\n")
                archivo_caso.write("\n")
                for d_col in casos_de_prueba[i][3]:
                    archivo_caso.write(f"{d_col}\n")
                archivo_caso.write("\n")
                for len_barco in casos_de_prueba[i][1]:
                    archivo_caso.write(f"{len_barco}\n")
            if (res_JJ/res_OPT) <= MAYOR_COTA_MIN_DESCUBIERTA_JJ:
                archivo_resultados_JJ.write(f"I={nombre_archivo_caso}, z(I)= {res_OPT}, A(I) = {res_JJ}, A(I)/z(I) = {(res_JJ/res_OPT)}\n")
            if (res_APROX/res_OPT) <= MAYOR_COTA_MIN_DESCUBIERTA_AP:
                archivo_resultados_AP.write(f"I={nombre_archivo_caso}, z(I)= {res_OPT}, A(I) = {res_APROX}, A(I)/z(I) = {(res_APROX/res_OPT)}\n")