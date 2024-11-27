from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

from bt import backtracking
from util import time_algorithm

# Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
seed(12345)
np.random.seed(12345)

sns.set_theme()


def medicion_bt(funcion_medicion, n_min, n_max, n_puntos, str_descripcion, str_nombre_archivo, complejidad_aprox):
        # La variable x van a ser los valores del eje x de los gráficos en todo el notebook
        # Tamaño mínimo=n_min, tamaño máximo=n_max, cantidad de puntos=n_puntos
        x = np.linspace(n_min, n_max, n_puntos).astype(int)
        results = time_algorithm(backtracking, x, lambda s: funcion_medicion(s))

        ax: plt.Axes
        fig, ax = plt.subplots()
        ax.plot(x, [results[i] for i in x], label="Medición")
        ax.set_title(f'Tiempo de ejecución del algoritmo de BT ({str_descripcion})')
        ax.set_xlabel('Valor de N')
        ax.set_ylabel('Tiempo de ejecución (s)')
        plt.savefig(f'bt_{str_nombre_archivo}_ejecucion.png', bbox_inches='tight')

        # scipy nos pide una función que recibe primero x y luego los parámetros a ajustar:
        f = lambda x, c1, c2: c1 * complejidad_aprox(x) + c2
        c, pcov = sp.optimize.curve_fit(f, x, [results[n] for n in x])
        print(f"c_1 = {c[0]}, c_2 = {c[1]}")
        r = np.sum((c[0] * complejidad_aprox(x) + c[1] - [results[n] for n in x])**2)
        print(f"Error cuadrático total: {r}")
        with open(f"bt_{str_nombre_archivo}_ajuste.txt", "w") as archivo:
            archivo.write(f"c_1 = {c[0]}, c_2 = {c[1]}\nError cuadratico total: {r}")

        ax.plot(x, [c[0] * complejidad_aprox(n) + c[1] for n in x], 'r--', label="Ajuste")
        ax.legend()
        plt.savefig(f'bt_{str_nombre_archivo}_ajuste.png', bbox_inches='tight')

        ax: plt.Axes
        fig, ax = plt.subplots()
        errors = [np.abs(c[0] * complejidad_aprox(n) + c[1] - results[n]) for n in x]
        ax.plot(x, errors)
        ax.set_title(f'Error de ajuste ({str_descripcion})')
        ax.set_xlabel('Valor de N')
        ax.set_ylabel('Error absoluto (s)')
        plt.savefig(f'bt_{str_nombre_archivo}_error.png', bbox_inches='tight')


if __name__ == '__main__': 
    def nfilas_ncolumnas_nbarcos(n):
        tablero = [[0 for _ in range(n)] for _ in range(n)]
        barcos = np.random.randint(1, n, n)
        d_filas = np.random.randint(1, n, n)
        d_columnas = np.random.randint(1, n, n)
        return [tablero, barcos, d_filas, d_columnas]

    def ctefilas_ctecolumnas_nbarcos(n):
        tablero = [[0 for _ in range(11)] for _ in range(11)]
        barcos = np.random.randint(1, 11, n)
        d_filas = np.random.randint(1, 11, 11)
        d_columnas = np.random.randint(1, 11, 11)
        return [tablero, barcos, d_filas, d_columnas]

    def nfilas_ncolumnas_ctebarcos(n):
        tablero = [[0 for _ in range(n)] for _ in range(n)]
        barcos = np.random.randint(1, 11, 11)
        d_filas = np.random.randint(1, n, n)
        d_columnas = np.random.randint(1, n, n)
        return [tablero, barcos, d_filas, d_columnas]

    def nfilas_ctecolumnas_nbarcos(n):
        tablero = [[0 for _ in range(3)] for _ in range(n)]
        barcos = np.random.randint(1, n, n)
        d_filas = np.random.randint(1, 3, n)
        d_columnas = np.random.randint(1, n, 3)
        return [tablero, barcos, d_filas, d_columnas]

    medicion_bt(nfilas_ncolumnas_nbarcos, 3, 11, 9, "N filas, columnas, y barcos", "ntodo", lambda n : (2**n))
    medicion_bt(ctefilas_ctecolumnas_nbarcos, 3, 11, 9, "N barcos", "nbarcos", lambda n : (2**n))
    medicion_bt(nfilas_ncolumnas_ctebarcos, 3, 11, 9, "N filas y columnas", "nfilcol", lambda n : (2**n))
    medicion_bt(nfilas_ctecolumnas_nbarcos, 3, 11, 9, "N filas y barcos", "nfilbarcos", lambda n : (2**n))


    input("Presione ENTER para terminar el programa")
