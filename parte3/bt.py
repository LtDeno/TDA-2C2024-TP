import parte3


def puedo_poner_barco(pos_ocupadas, indice, barco, fil, col, horizontal):
    if pos_ocupadas[fil][col]:
        return False

    if horizontal:
        if col + barco > len(pos_ocupadas[0]):
            return False

        for i in range(barco):
            if pos_ocupadas[fil][col + i]:
                return False
    else:
        if fil + barco > len(pos_ocupadas):
            return False

        for i in range(barco):
            if pos_ocupadas[fil + i][col]:
                return False

    return True


def poner_barco(pos_ocupadas, indice, barco, asignacion_actual, fil, col, horizontal):
    if horizontal:
        fil_sup = fil if fil <= 0 else fil - 1
        fil_inf = fil if fil >= len(pos_ocupadas) - 1 else fil + 1
        col_izq = col if col <= 0 else col - 1
        col_der = barco if col + barco >= len(pos_ocupadas[0]) else barco + 1

        for i in range(col_izq, col_der):
            pos_ocupadas[fil][col + i] = True
            pos_ocupadas[fil_sup][col + i] = True
            pos_ocupadas[fil_inf][col + i] = True

        asignacion_actual[indice] = parte3.gen_asignacion(fil, fil, col + barco - 1, col)

    else:
        col_izq = col if col <= 0 else col - 1
        col_der = col if col >= len(pos_ocupadas[0]) - 1 else col + 1
        fil_sup = fil if fil <= 0 else fil - 1
        fil_inf = barco if fil + barco >= len(pos_ocupadas) else barco + 1

        for i in range(fil_sup, fil_inf):
            pos_ocupadas[fil + i][col] = True
            pos_ocupadas[fil + i][col_izq] = True
            pos_ocupadas[fil + i][col_der] = True

        asignacion_actual[indice] = parte3.gen_asignacion(fil + barco - 1, fil, col, col)


def sacar_barco(pos_ocupadas, indice, barco, asignacion_actual, fil, col, horizontal):
    if horizontal:
        fil_sup = fil if fil <= 0 else fil - 1
        fil_inf = fil if fil >= len(pos_ocupadas) - 1 else fil + 1
        col_izq = col if col <= 0 else col - 1
        col_der = barco if col + barco >= len(pos_ocupadas[0]) else barco + 1

        for i in range(col_izq, col_der):
            pos_ocupadas[fil][col + i] = False
            pos_ocupadas[fil_sup][col + i] = False
            pos_ocupadas[fil_inf][col + i] = False

        asignacion_actual.pop(indice)

    else:
        col_izq = col if col <= 0 else col - 1
        col_der = col if col >= len(pos_ocupadas[0]) - 1 else col + 1
        fil_sup = fil if fil <= 0 else fil - 1
        fil_inf = barco if fil + barco >= len(pos_ocupadas) else barco + 1

        for i in range(fil_sup, fil_inf):
            pos_ocupadas[fil + i][col] = False
            pos_ocupadas[fil + i][col_izq] = False
            pos_ocupadas[fil + i][col_der] = False

        asignacion_actual.pop(indice)


def calcular_demandas_cumplidas(asignaciones):
    sumatoria = 0
    for v in asignaciones.values():
        sumatoria += (abs(v[0][0] - v[1][0]) + abs(v[0][1] - v[1][1]) + 1) * 2
    return sumatoria


def bt_recursivo(pos_ocupadas, indice, barcos, barcos_a_omitir, d_filas, d_columnas, asignacion_actual, mejor_asignacion):
    if indice == len(barcos):
        demanda_cumplida_actual = calcular_demandas_cumplidas(asignacion_actual)
        if mejor_asignacion[1] < demanda_cumplida_actual:
            mejor_asignacion[0] = asignacion_actual.copy()
            mejor_asignacion[1] = demanda_cumplida_actual
        return

    barco = barcos[indice]

    if not barcos_a_omitir[indice]:
        for fil in range(len(d_filas)):
            for col in range(len(d_columnas)):
                if puedo_poner_barco(pos_ocupadas, indice, barco, fil, col, True):
                    poner_barco(pos_ocupadas, indice, barco, asignacion_actual, fil, col, True)
                    bt_recursivo(pos_ocupadas, indice + 1, barcos, barcos_a_omitir, d_filas, d_columnas, asignacion_actual, mejor_asignacion)
                    sacar_barco(pos_ocupadas, indice, barco, asignacion_actual, fil, col, True)

                if puedo_poner_barco(pos_ocupadas, indice, barco, fil, col, False):
                    poner_barco(pos_ocupadas, indice, barco, asignacion_actual, fil, col, False)
                    bt_recursivo(pos_ocupadas, indice + 1, barcos, barcos_a_omitir, d_filas, d_columnas, asignacion_actual, mejor_asignacion)
                    sacar_barco(pos_ocupadas, indice, barco, asignacion_actual, fil, col, False)


def pos_ocupadas_inicial(tablero):
    return [[False for _ in range(len(tablero[0]))] for _ in range(len(tablero))]


def barcos_demasiado_largos(barcos, d_filas, d_columnas):
    maximo = max(max(d_filas), max(d_columnas))
    a_omitir = []
    for b in barcos:
        if b <= maximo:
            a_omitir.append(False)
            continue
        a_omitir.append(True)

    return a_omitir


def mostrar_tablero(asignaciones, d_filas, d_columnas):
    tab = [["-" for _ in range(len(d_columnas))] for _ in range(len(d_filas))]
    for key in asignaciones.keys():
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


def backtracking(tablero, barcos, d_filas, d_columnas):  # Lautaro
    mejor_asignacion = [{}, float('-inf')]

    bt_recursivo(pos_ocupadas_inicial(tablero), 0, barcos, barcos_demasiado_largos(barcos, d_filas, d_columnas),
                 d_filas, d_columnas, {}, mejor_asignacion)

    mostrar_tablero(mejor_asignacion[0], d_filas, d_columnas)
    return mejor_asignacion[0]
