from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

from parte2 import pdinamica
from parte2 import reconstruccion
from util import time_algorithm

# Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
seed(12345)
np.random.seed(12345)

sns.set_theme()

def medicion_pd(algoritmo, funcion_medicion, n_min, n_max, n_puntos, str_descripcion, str_nombre_archivo, complejidad_aprox):
        # La variable x van a ser los valores del eje x de los gráficos en todo el notebook
        # Tamaño mínimo=n_min, tamaño máximo=n_max, cantidad de puntos=n_puntos
        x = np.linspace(n_min, n_max, n_puntos).astype(int)
        results = time_algorithm(algoritmo, x, lambda s: funcion_medicion(s))

        ax: plt.Axes
        fig, ax = plt.subplots()
        ax.plot(x, [results[i] for i in x], label="Medición")
        ax.set_title(f'{str_descripcion}')
        ax.set_xlabel('Tamaño del array de monedas')
        ax.set_ylabel('Tiempo de ejecución (s)')
        plt.savefig(f'{str_nombre_archivo}_ejecucion.png', bbox_inches='tight')

        # scipy nos pide una función que recibe primero x y luego los parámetros a ajustar:
        f = lambda x, c1, c2: c1 * complejidad_aprox(x) + c2
        c, pcov = sp.optimize.curve_fit(f, x, [results[n] for n in x])
        print(f"c_1 = {c[0]}, c_2 = {c[1]}")
        r = np.sum((c[0] * complejidad_aprox(x) + c[1] - [results[n] for n in x])**2)
        print(f"Error cuadrático total: {r}")
        with open(f"{str_nombre_archivo}_ajuste.txt", "w") as archivo:
            archivo.write(f"c_1 = {c[0]}, c_2 = {c[1]}\nError cuadratico total: {r}")

        ax.plot(x, [c[0] * complejidad_aprox(n) + c[1] for n in x], 'r--', label="Ajuste")
        ax.legend()
        plt.savefig(f'{str_nombre_archivo}_ajuste.png', bbox_inches='tight')

        ax: plt.Axes
        fig, ax = plt.subplots()
        errors = [np.abs(c[0] * complejidad_aprox(n) + c[1] - results[n]) for n in x]
        ax.plot(x, errors)
        ax.set_title(f'Error de ajuste ({str_descripcion})')
        ax.set_xlabel('Tamaño del array de monedas')
        ax.set_ylabel('Error absoluto (s)')
        plt.savefig(f'{str_nombre_archivo}_error.png', bbox_inches='tight')


if __name__ == '__main__':
    def obtener_monedas_aleatorias(size: int):
        return [np.random.randint(1, 1000, size)]
    
    def obtener_problemas_resueltos_random(size: int):
        monedas = np.random.randint(1, 1000, size)
        tabla = pdinamica(monedas)
        return [monedas, tabla] #TODO: Ver si la obtención de estos problemas resueltos interfiere con las mediciones
    
    medicion_pd(pdinamica, obtener_monedas_aleatorias, 20, 1000, 20, "Algoritmo Programación Dinámica", "pd_tabla_opts", lambda n : n**2)
    medicion_pd(reconstruccion, obtener_problemas_resueltos_random, 20, 1000, 20, "Algoritmo Reconstrucción de OPTs de PD", "pd_reconstruccion", lambda n : n)

    input("Presione ENTER para terminar el programa")