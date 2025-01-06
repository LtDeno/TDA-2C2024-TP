def tiene_adyacentes(tablero, coords_final, coords_inicial, longitud, vertical:bool):
    if vertical:
        inicio = -1 if coords_inicial[0] > 0 else 0
        fin = longitud + 1 if coords_inicial[0] + longitud < len(tablero) else longitud
        for i in range(inicio, fin):
            x = coords_inicial[0] + i
            for j in range(max(0, coords_inicial[1] - 1), min(len(tablero[0]), coords_inicial[1] + 2)):
                if j == coords_inicial[1] and (coords_inicial[0] <= x <= coords_final[0]):
                    continue
                if tablero[x][j]:
                    return True

    else:
        inicio = -1 if coords_inicial[1] > 0 else 0
        fin = longitud + 1 if coords_inicial[1] + longitud <= len(tablero[0]) else longitud
        for j in range(inicio, fin):
            y = coords_inicial[1] + j
            for i in range(max(0, coords_inicial[0] - 1), min(len(tablero), coords_inicial[0] + 2)):
                if i == coords_inicial[0] and (coords_inicial[1] <= y <= coords_final[1]):
                    continue
                if tablero[i][y]:
                    return True
    return False

def se_puede_poner_barco(coords_final, coords_inicial, tablero):
    # Está puesto vertical.
    if coords_final[1] == coords_inicial[1]:
        longitud = abs(coords_final[0] - coords_inicial[0]) + 1
        for i in range(longitud):
            if tablero[coords_inicial[0] + i][coords_inicial[1]]:

                return False
            tablero[coords_inicial[0] + i][coords_inicial[1]] = True
        if tiene_adyacentes(tablero, coords_final, coords_inicial, longitud, True):
            print("tiene adyacentes")
            return False

    # Está puesto horizontal.
    else:
        longitud = abs(coords_final[1] - coords_inicial[1]) + 1
        for j in range(longitud):
            if tablero[coords_inicial[0]][coords_inicial[1] + j]:
                return False
            tablero[coords_inicial[0]][coords_inicial[1] + j] = True
        if tiene_adyacentes(tablero, coords_final, coords_inicial, longitud, False):
            return False

    return True

def validar(barcos_disponibles, demanda_filas, demanda_columnas, asignaciones):
    if len(barcos_disponibles) != len(asignaciones):
        return False

    tablero = [[False for _ in range(len(demanda_columnas))] for _ in range(len(demanda_filas))]
    filas = demanda_filas.copy()
    columnas = demanda_columnas.copy()

    # Colocar barcos para comprobar colisiones y adyacencia
    for key in asignaciones.keys():
        coords = asignaciones[key]
        if coords is not None:
            if not se_puede_poner_barco(coords[0], coords[1], tablero):
                return False

    # Contar demandas satisfechas
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j]:
                filas[i] -= 1
                columnas[j] -= 1

    # Buscar demandas sobresatisfechas y/o demandas insatisfechas
    for num in filas:
        if num < 0 or num > 0:
            return False
    for num in columnas:
        if num < 0 or num > 0:
            return False

    # Validado en tiempo polinomial.
    # No tiene colisiones o barcos adyacentes, no tiene demandas sobresatisfechas o insatisfechas.
    return True
