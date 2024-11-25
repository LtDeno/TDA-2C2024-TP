def johnjellicoe(tablero, barcos, d_filas, d_columnas):
    """
    Algoritmo John Jellicoe:
        - Va a fila/columna de mayor demanda y ubica el barco de mayor longitud en dicha fila/columna en algún lugar válido. 
        - Si el barco de mayor longitud es más largo que dicha demanda, saltea ese barco y continua con el siguiente de la lista.
        - Vuelve a probar hasta que no queden más barcos por probar o no haya más demandas por cumplir.
    """
    d_filas_restantes = d_filas[:]
    d_columnas_restantes = d_columnas[:]
    barcos.sort(reverse=True)
    asignaciones = colocar_barcos(tablero, barcos, d_filas_restantes, d_columnas_restantes)
    imprimir_tablero(tablero)

    return asignaciones

def colocar_barcos(tablero, barcos, d_filas_restantes, d_columnas_restantes):
    """
    Intenta colocar cada barco en el tablero, priorizando la fila o columna con mayor demanda.
    Si no se puede colocar un barco, se pasa al siguiente.
    """
    asignaciones = {i: None for i in range(len(barcos))}

    for i, barco in enumerate(barcos):
        colocado = False
        fila = seleccionar_fila(d_filas_restantes)
        columna = seleccionar_columna(d_columnas_restantes)

        # Imprimo los pasos p/ debug..
        # print(f"\nBarco de longitud {barco}:")
        # print(f"Fila con mayor demanda: Fila {fila}, Demanda {d_filas_restantes[fila]}")
        # print(f"Columna con mayor demanda: Columna {columna}, Demanda {d_columnas_restantes[columna]}")

        if d_filas_restantes[fila] >= d_columnas_restantes[columna]:
            for col in range(len(tablero[0])):
                if puedo_colocar_el_barco(tablero, d_filas_restantes, d_columnas_restantes, fila, col, barco, True):
                    colocar_barco(tablero, d_filas_restantes, d_columnas_restantes, fila, col, barco, True)
                    asignaciones[i] = [(fila, col), (fila, col + barco - 1)]
                    colocado = True
                    # print(f"Barco colocado horizontalmente en fila {fila}, desde columna {col} hasta columna {col + barco - 1}")
                    break
        else:
            for row in range(len(tablero)):
                if puedo_colocar_el_barco(tablero, d_filas_restantes, d_columnas_restantes, row, columna, barco, False):
                    colocar_barco(tablero, d_filas_restantes, d_columnas_restantes, row, columna, barco, False)
                    asignaciones[i] = [(row, columna), (row + barco - 1, columna)]
                    colocado = True
                    # print(f"Barco colocado verticalmente en columna {columna}, desde fila {row} hasta fila {row + barco - 1}")
                    break

        # Si el barco no pudo colocarse, se pasa al siguiente barco..
        if not colocado:
            # print(f"Barco de longitud {barco} no entró en el tablero.")
            continue

    return asignaciones

def seleccionar_fila(d_filas_restantes):
    """
    Selecciona la fila con la mayor demanda restante.
    """
    return max(range(len(d_filas_restantes)), key=lambda i: d_filas_restantes[i])

def seleccionar_columna(d_columnas_restantes):
    """
    Selecciona la columna con la mayor demanda restante.
    """
    return max(range(len(d_columnas_restantes)), key=lambda i: d_columnas_restantes[i])

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
