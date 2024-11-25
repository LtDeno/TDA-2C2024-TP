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
                y_celdas_ocupadas_barcos[b][i].append(pulp.LpVariable("y_" + str(b) + "_" + str(i) + "_" + str(j), cat="Binary"))


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

    mostrar_tabla(y_celdas_ocupadas_barcos)

    # TRADUCCIÓN DEL RESULTADO
    resultado = {}
    for b in range(cant_bar):
        resultado[b] = None
        barco_encontrado = False
        for i in range(cant_fil):
            for j in range(cant_col):
                if pulp.value(y_celdas_ocupadas_barcos[b][i][j]) == 1.0:
                    barco_encontrado = True
                    resultado[b] = [(i, j)]
                    #if barcos[b] > 1:
                    if (i < cant_fil-1) and (pulp.value(y_celdas_ocupadas_barcos[b][i+1][j]) == 1.0):
                        resultado[b].append((i + barcos[b] - 1, j))
                    else:
                        resultado[b].append((i, j + barcos[b] - 1))
                    break
            if barco_encontrado:
                break

    return resultado



def mostrar_tabla(y_celdas_ocupadas_barcos):
    tab = [["-" for _ in range(len(y_celdas_ocupadas_barcos[0]))] for _ in range(len(y_celdas_ocupadas_barcos[0][0]))]
    for b in range(len(y_celdas_ocupadas_barcos)):
        for i in range(len(y_celdas_ocupadas_barcos[0])):
            for j in range(len(y_celdas_ocupadas_barcos[0][0])):
                if pulp.value(y_celdas_ocupadas_barcos[b][i][j]) == 1.0:
                    tab[i][j] = str(b)
    for t in tab:
        print(t)