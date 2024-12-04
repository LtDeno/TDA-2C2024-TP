import copy
import parte3
import time


def puedo_poner_barco(pos_ocupadas, t_barco, d_filas_restantes, d_columnas_restantes, fil, col, horizontal):
    if pos_ocupadas[fil][col]:
        return False

    if horizontal:
        if col + t_barco[1] > len(pos_ocupadas[0]):
            return False
        
        if d_filas_restantes[fil] - t_barco[1] < 0:
            return False
        
        for i in range(t_barco[1]):
            if d_columnas_restantes[col + i] - 1 < 0:
                return False

        for i in range(-1, 2):
            f = 0 if (fil + i < 0 or fil + i >= len(pos_ocupadas)) else i
            for j in range(-1, t_barco[1] + 2):
                c = 0 if (col + j < 0 or col + j >= len(pos_ocupadas[0])) else j
                if pos_ocupadas[fil + f][col + c]:
                    return False

    else:
        if fil + t_barco[1] > len(pos_ocupadas):
            return False
        
        if d_columnas_restantes[col] - t_barco[1] < 0:
            return False
        
        for i in range(t_barco[1]):
            if d_filas_restantes[fil + i] - 1 < 0:
                return False

        for i in range(-1, t_barco[1] + 2):
            f = 0 if (fil + i < 0 or fil + i >= len(pos_ocupadas)) else i
            for j in range(-1, 2):
                c = 0 if (col + j < 0 or col + j >= len(pos_ocupadas[0])) else j
                if pos_ocupadas[fil + f][col + c]:
                    return False

    return True


def poner_barco(pos_ocupadas, t_barco, d_filas_restantes,  d_columnas_restantes, asignacion_actual, fil, col, horizontal):
    if horizontal:
        for i in range(t_barco[1]):
            pos_ocupadas[fil][col + i] = True
            d_columnas_restantes[col + i] -= 1
        d_filas_restantes[fil] -= t_barco[1]

        asignacion_actual[t_barco[0]] = parte3.gen_asignacion(fil, fil, col + t_barco[1] - 1, col)

    else:
        for i in range(t_barco[1]):
            pos_ocupadas[fil + i][col] = True
            d_filas_restantes[fil + i] -= 1
        d_columnas_restantes[col] -= t_barco[1]

        asignacion_actual[t_barco[0]] = parte3.gen_asignacion(fil + t_barco[1] - 1, fil, col, col)


def sacar_barco(pos_ocupadas, t_barco, d_filas_restantes,  d_columnas_restantes, asignacion_actual, fil, col, horizontal):
    if horizontal:
        for i in range(t_barco[1]):
            pos_ocupadas[fil][col + i] = False
            d_columnas_restantes[col + i] += 1
        d_filas_restantes[fil] += t_barco[1]

        asignacion_actual.pop(t_barco[0])

    else:
        for i in range(t_barco[1]):
            pos_ocupadas[fil + i][col] = False
            d_filas_restantes[fil + i] += 1
        d_columnas_restantes[col] += t_barco[1]

        asignacion_actual.pop(t_barco[0])


def calcular_demandas_cumplidas(asignaciones):
    sumatoria = 0
    for v in asignaciones.values():
        sumatoria += (abs(v[0][0] - v[1][0]) + abs(v[0][1] - v[1][1]) + 1) * 2
    return sumatoria


def ya_no_llego(asignacion_actual, mejor_demanda_cumplida, long_barcos_restante):
    if calcular_demandas_cumplidas(asignacion_actual) + (long_barcos_restante*2) > mejor_demanda_cumplida:
        return False
    return True


def bt_recursivo(pos_ocupadas, indice, barcos, barcos_a_omitir, d_filas, d_columnas, d_filas_restantes, d_columnas_restantes, asignacion_actual, mejor_asignacion, long_barcos_restante):
    if indice == len(barcos):
        demanda_cumplida_actual = calcular_demandas_cumplidas(asignacion_actual)
        if mejor_asignacion[1] < demanda_cumplida_actual:
            mejor_asignacion[0] = asignacion_actual.copy()
            mejor_asignacion[1] = demanda_cumplida_actual
        return

    if ya_no_llego(asignacion_actual, mejor_asignacion[1], long_barcos_restante):
        return

    t_barco = barcos[indice]

    if not barcos_a_omitir[indice]:
        for fil in range(len(d_filas)):
            for col in range(len(d_columnas)):
                if puedo_poner_barco(pos_ocupadas, t_barco, d_filas_restantes, d_columnas_restantes, fil, col, True):
                    poner_barco(pos_ocupadas, t_barco, d_filas_restantes, d_columnas_restantes, asignacion_actual, fil, col, True)
                    bt_recursivo(pos_ocupadas, indice + 1, barcos, barcos_a_omitir, d_filas, d_columnas, d_filas_restantes, d_columnas_restantes, asignacion_actual, mejor_asignacion, long_barcos_restante - t_barco[1])
                    sacar_barco(pos_ocupadas, t_barco, d_filas_restantes, d_columnas_restantes, asignacion_actual, fil, col, True)

                if puedo_poner_barco(pos_ocupadas, t_barco, d_filas_restantes, d_columnas_restantes, fil, col, False):
                    poner_barco(pos_ocupadas, t_barco, d_filas_restantes, d_columnas_restantes, asignacion_actual, fil, col, False)
                    bt_recursivo(pos_ocupadas, indice + 1, barcos, barcos_a_omitir, d_filas, d_columnas, d_filas_restantes, d_columnas_restantes, asignacion_actual, mejor_asignacion, long_barcos_restante - t_barco[1])
                    sacar_barco(pos_ocupadas, t_barco, d_filas_restantes, d_columnas_restantes, asignacion_actual, fil, col, False)

    bt_recursivo(pos_ocupadas, indice + 1, barcos, barcos_a_omitir, d_filas, d_columnas, d_filas_restantes, d_columnas_restantes, asignacion_actual, mejor_asignacion, long_barcos_restante - t_barco[1])


def pos_ocupadas_inicial(tablero):
    return [[False for _ in range(len(tablero[0]))] for _ in range(len(tablero))]


def barcos_demasiados_largos(tuplas_barcos, d_filas, d_columnas):
    maximo = max(max(d_filas), max(d_columnas))
    a_omitir = []
    for b in tuplas_barcos:
        if b[1] <= maximo:
            a_omitir.append(False)
        else:
            a_omitir.append(True)

    return a_omitir


def ordenar_en_tuplas(barcos):
    barcos_ordenados = []
    for i in range(len(barcos)):
        barcos_ordenados.append((i, barcos[i]))

    barcos_ordenados.sort(reverse=True, key=lambda tupla: tupla[1])
    return barcos_ordenados


def reconstruir_asignaciones(asignaciones, n_barcos):
    reconstruido = {}
    for i in range(n_barcos):
        if i in asignaciones:
            reconstruido[i] = asignaciones[i]
        else:
            reconstruido[i] = None
    return reconstruido


def sumar_longitudes(barcos):
    sumatoria = 0
    for b in barcos:
        sumatoria += b
    return sumatoria


def mostrar_tablero(asignaciones, d_filas, d_columnas):
    tab = [["-" for _ in range(len(d_columnas))] for _ in range(len(d_filas))]
    for key in asignaciones.keys():
        if asignaciones[key] is not None:
            desplazamiento = (asignaciones[key][0][0] - asignaciones[key][1][0], asignaciones[key][0][1] - asignaciones[key][1][1])
            if desplazamiento[0] == 0:
                for i in range(desplazamiento[1]+1):
                    tab[asignaciones[key][1][0]][asignaciones[key][1][1] + i] = str(key)
            else:
                for i in range(desplazamiento[0]+1):
                    tab[asignaciones[key][1][0] + i][asignaciones[key][1][1]] = str(key)

    print()
    for t in tab:
        print(t)


def backtracking(tablero, barcos, d_filas, d_columnas):
    s = time.time()

    mejor_asignacion = [{}, float('-inf')]
    bt_recursivo(pos_ocupadas_inicial(tablero), 0, ordenar_en_tuplas(barcos), barcos_demasiados_largos(ordenar_en_tuplas(barcos), d_filas, d_columnas),
                 d_filas, d_columnas, copy.deepcopy(d_filas), copy.deepcopy(d_columnas), {}, mejor_asignacion, sumar_longitudes(barcos))

    mejor_asignacion[0] = reconstruir_asignaciones(mejor_asignacion[0], len(barcos))

    f = time.time()
    print(f-s)
    mostrar_tablero(mejor_asignacion[0], d_filas, d_columnas)
    return mejor_asignacion[0]
