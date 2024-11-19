import pulp
from pulp import LpAffineExpression as Sumatoria


def proglineal(tablero, barcos, d_filas, d_columnas):  # Matias
    problem = pulp.LpProblem("Problema de Barcos", pulp.LpMaximize)

    cant_bar = len(barcos)
    cant_fil = len(tablero)
    cant_col = len(tablero[0])

    # VARIABLES
    # y_b_i_j : La casilla ij está ocupada por el barco b
    y_celdas_ocupadas_barcos = [] #Matriz cubica que tiene una cantidad de elementos igual a barcos*filas*columnas
    for b in range(cant_bar):
        y_celdas_ocupadas_barcos.append([])
        for i in range(cant_fil):
            y_celdas_ocupadas_barcos[b].append([])
            for j in range(cant_col):
                y_celdas_ocupadas_barcos[i].append(pulp.LpVariable("y_" + str(b) + "_" + str(i) + "_" + str(j), cat="Binary"))


    # RESTRICCIONES:
    # - Que lo ocupado en filas y columnas no exceda la demanda de las mismas
    for i in range(cant_fil):
        terminos_sumatoria = []
        for b in range(cant_bar):
            for j in range(cant_col):
                terminos_sumatoria.append((y_celdas_ocupadas_barcos[b][i][j], 1))
        problem += Sumatoria(terminos_sumatoria) <= d_filas[i]
    
    for j in range(cant_col):
        terminos_sumatoria = []
        for b in range(cant_bar):
            for i in range(cant_fil):
                terminos_sumatoria.append((y_celdas_ocupadas_barcos[b][i][j], 1))
        problem += Sumatoria(terminos_sumatoria) <= d_columnas[j]

    # - Si una celda ij está ocupada por un barco de largo L, entonces deben haber por lo menos L-1 celdas ocupadas en una cruz (celdas horizontales y verticales) de L-1 de distancia a esta celda ij
    for b in range(cant_bar):
        for i in range(cant_fil):
            for j in range(cant_col):
                terminos_sumatoria = []
                for i_b in range(max(i-barcos[b]+1, 0), i):
                    terminos_sumatoria.append((y_celdas_ocupadas_barcos[b][i_b][j], 1))
                for i_b in range(i+1, min(i+barcos[b], cant_col - 1)):
                    terminos_sumatoria.append((y_celdas_ocupadas_barcos[b][i_b][j], 1))
                for j_b in range(max(j-barcos[b]+1, 0), j):
                    terminos_sumatoria.append((y_celdas_ocupadas_barcos[b][i][j_b], 1))
                for j_b in range(j+1, min(j+barcos[b], cant_col - 1)):
                    terminos_sumatoria.append((y_celdas_ocupadas_barcos[b][i][j_b], 1))
                # problem += Sumatoria(terminos_sumatoria) <= ((barcos[b] - 1) - 1 + y_celdas_ocupadas_barcos[b][i][j]) # (?) ESTA RESTRICCIÓN PODRÍA ROMPERSE EN CASO DE y_celdas_ocupadas_barcos[b][i][j] = 0. ADEMÁS, ESTA RESTRICCIÓN ES REDUNDANTE CON LA SIGUIENTE
                problem += Sumatoria(terminos_sumatoria) >= ((barcos[b] - 1) * y_celdas_ocupadas_barcos[b][i][j])

    # La cantidad de celdas ocupadas por un barco de largo L no puede superar las L celdas
    for b in range(cant_bar):
        terminos_sumatoria = []
        for i in range(cant_fil):
            for j in range(cant_col):
                terminos_sumatoria.append((y_celdas_ocupadas_barcos[b][i][j], 1))
        problem += Sumatoria(terminos_sumatoria) <= barcos[b]

    # Una celda ocupada por un barco no puede estar adyacente (o diagonalmente adyacente) a una celda ocupada por otro barco
    for b in range(cant_bar-1):
        for i in range(cant_fil):
            for j in range(cant_col):
                terminos_sumatoria = []
                for b_aux in range(b+1, cant_bar):
                    for i_aux in range(max(i-1, 0), min(i+2, cant_col - 1)):
                        for j_aux in range(max(i-1, 0), min(i+2, cant_col - 1)):
                            terminos_sumatoria.append((y_celdas_ocupadas_barcos[b_aux][i_aux][j_aux], 1))
                problem += Sumatoria(terminos_sumatoria) <= 9 * (1 - y_celdas_ocupadas_barcos[b][i][j])


    # FUNCIÓN OBJETIVO
    # Maximizar la cantidad de casillas ocupadas por barcos
    terminos_sumatoria = []
    for b in range(cant_bar):
        for i in range(cant_fil):
            for j in range(cant_col):
                terminos_sumatoria.append((y_celdas_ocupadas_barcos[b][i][j], 1))
    problem += Sumatoria(terminos_sumatoria)
    problem.solve()


    # TRADUCCIÓN DEL RESULTADO
    # TODO
    resultado = {}

    return resultado
