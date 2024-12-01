from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

from parte1 import greedy
from util import time_algorithm

# Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
seed(12345)
np.random.seed(12345)

sns.set_theme()


if __name__ == '__main__': 
    def get_random_array(size: int):
        return np.random.randint(1, 1000, size)
    # La variable x van a ser los valores del eje x de los gráficos en todo el notebook
    # Tamaño mínimo=100, tamaño máximo=20k, cantidad de puntos=20
    x = np.linspace(20, 20000, 20).astype(int)
    results = time_algorithm(greedy, x, lambda s: [get_random_array(s)])



    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución del algoritmo Greedy')
    ax.set_xlabel('Tamaño del array de monedas')
    ax.set_ylabel('Tiempo de ejecución (s)')
    plt.savefig('greedy_ejecucion.png', bbox_inches='tight')



    # scipy nos pide una función que recibe primero x y luego los parámetros a ajustar:
    f = lambda x, c1, c2: c1 * x + c2
    c, pcov = sp.optimize.curve_fit(f, x, [results[n] for n in x])
    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.sum((c[0] * x + c[1] - [results[n] for n in x])**2)
    print(f"Error cuadrático total: {r}")
    with open("greedy_ajuste.txt", "w") as archivo:
        archivo.write(f"c_1 = {c[0]}, c_2 = {c[1]}\nError cuadratico total: {r}")



    ax.plot(x, [c[0] * n + c[1] for n in x], 'r--', label="Ajuste")
    ax.legend()
    fig
    plt.savefig('greedy_ajuste.png', bbox_inches='tight')



    ax: plt.Axes
    fig, ax = plt.subplots()
    errors = [np.abs(c[0] * n + c[1] - results[n]) for n in x]
    ax.plot(x, errors)
    ax.set_title('Error de ajuste')
    ax.set_xlabel('Tamaño del array de monedas')
    ax.set_ylabel('Error absoluto (s)')
    plt.savefig('greedy_error.png', bbox_inches='tight')


    input("Presione ENTER para terminar el programa")