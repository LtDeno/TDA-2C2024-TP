from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

from bt import backtracking
from pl import proglineal
from util import time_algorithm

# Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
seed(12345)
np.random.seed(12345)

sns.set_theme()

def nfilas_ncolumnas_nbarcos(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    barcos = np.random.randint(1, n, n)
    d_filas = np.random.randint(1, n, n)
    d_columnas = np.random.randint(1, n, n)
    return [tablero, barcos, d_filas, d_columnas]

if __name__ == '__main__':
    N_MIN = 3 
    N_MAX = 7
    N_PUNTOS = 5

    x = np.linspace(N_MIN, N_MAX, N_PUNTOS).astype(int)
    results_bt = time_algorithm(backtracking, x, lambda s: nfilas_ncolumnas_nbarcos(s))
    results_pl = time_algorithm(proglineal, x, lambda s: nfilas_ncolumnas_nbarcos(s))

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results_bt[i] for i in x], label="Medición BT")
    ax.plot(x, [results_pl[i] for i in x], label="Medición PL")
    ax.legend()
    ax.set_title(f'Tiempo de ejecución del algoritmo de BT vs PL (N filas, columnas, y barcos)')
    ax.set_xlabel('Valor de N')
    ax.set_ylabel('Tiempo de ejecución (s)')
    plt.savefig(f'bt_vs_pl_ejecucion.png', bbox_inches='tight')