def aproximacion(tablero, barcos, d_filas, d_columnas):
    """
    El algoritmo propuesto sigue la regla de "colocar primero los barcos pequeños en la primera posición válida, cumpliendo con las restricciones
    del tablero y las demandas restantes".
    Esto lo hace priorizando las decisiones locales inmediatas y esperando que dichas decisiones conduzcan a una óptima solución global.
    """
    d_filas_restantes = d_filas[:]
    d_columnas_restantes = d_columnas[:]
    barcos.sort()
    asignaciones = colocar_barcos(tablero, barcos, d_filas_restantes, d_columnas_restantes)
    imprimir_tablero(tablero)

    return asignaciones

def colocar_barcos(tablero, barcos, d_filas_restantes, d_columnas_restantes):
    """
    Intenta colocar cada barco en el tablero, cumpliendo las restricciones.
    """
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
    """
    Verifica si un barco puede colocarse en la posición especificada.
    """
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
    """
    Coloca un barco en el tablero y actualiza las demandas restantes.
    """
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
    """
    Verifica si una celda es válida para colocar el barco.
    """
    if tablero[fila][columna] != 0:
        return False
    for df in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nf, nc = fila + df, columna + dc
            if 0 <= nf < len(tablero) and 0 <= nc < len(tablero[0]) and tablero[nf][nc] != 0:
                return False
    return True

def imprimir_tablero(tablero):
    """
    Imprime el tablero.
    """
    print("\nTablero final:")
    for fila in tablero:
        print(" ".join(map(str, fila)))
