import copy


def aproximacion(tablero, barcos, d_filas, d_columnas):
    tablero_resultado = copy.deepcopy(tablero)
    d_filas_restantes = copy.deepcopy(d_filas)
    d_columnas_restantes = copy.deepcopy(d_columnas)
    asignaciones = colocar_barcos(tablero_resultado, sorted(barcos, reverse=True), d_filas_restantes, d_columnas_restantes)
    imprimir_tablero(tablero_resultado)

    return asignaciones


def colocar_barcos(tablero, barcos, d_filas_restantes, d_columnas_restantes):
    asignaciones = {i: None for i in range(len(barcos))}

    for i, barco in enumerate(barcos):
        colocado = False
        for fila in range(len(tablero)):
            for columna in range(len(tablero[0])):
                if puedo_colocar_el_barco(tablero, d_filas_restantes, d_columnas_restantes, fila, columna, barco, True):
                    colocar_barco(tablero, d_filas_restantes, d_columnas_restantes, fila, columna, barco, True)
                    asignaciones[i] = [(fila, columna), (fila, columna + barco - 1)]
                    colocado = True
                    break
                if puedo_colocar_el_barco(tablero, d_filas_restantes, d_columnas_restantes, fila, columna, barco, False):
                    colocar_barco(tablero, d_filas_restantes, d_columnas_restantes, fila, columna, barco, False)
                    asignaciones[i] = [(fila, columna), (fila + barco - 1, columna)]
                    colocado = True
                    break
            if colocado:
                break

    return asignaciones


def puedo_colocar_el_barco(tablero, d_filas_restantes, d_columnas_restantes, fila, columna, longitud, horizontal):
    if horizontal:
        if columna + longitud > len(tablero[0]):
            return False
        if d_filas_restantes[fila] < longitud:
            return False
        for c in range(columna, columna + longitud):
            if d_columnas_restantes[c] < 1 or not posicion_valida(tablero, fila, c):
                return False
    else:
        if fila + longitud > len(tablero):
            return False
        if d_columnas_restantes[columna] < longitud:
            return False
        for f in range(fila, fila + longitud):
            if d_filas_restantes[f] < 1 or not posicion_valida(tablero, f, columna):
                return False
    return True


def colocar_barco(tablero, d_filas_restantes, d_columnas_restantes, fila, columna, longitud, horizontal):
    if horizontal:
        for c in range(columna, columna + longitud):
            tablero[fila][c] = 1
            d_columnas_restantes[c] -= 1
        d_filas_restantes[fila] -= longitud
    else:
        for f in range(fila, fila + longitud):
            tablero[f][columna] = 1
            d_filas_restantes[f] -= 1
        d_columnas_restantes[columna] -= longitud


def posicion_valida(tablero, fila, columna):
    if tablero[fila][columna] != 0:
        return False
    for df in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nf, nc = fila + df, columna + dc
            if 0 <= nf < len(tablero) and 0 <= nc < len(tablero[0]) and tablero[nf][nc] != 0:
                return False
    return True


def imprimir_tablero(tablero):
    print("\nTablero final:")
    for fila in tablero:
        print(" ".join(map(str, fila)))
