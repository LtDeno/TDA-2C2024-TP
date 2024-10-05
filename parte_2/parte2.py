import sys


def turno_mateo_greedy(arr_turnos, arr_monedas, arr_datos):
    if arr_datos[0] > arr_datos[len(arr_datos) - 1]:
        arr_turnos.append("Mateo agarra la primera (" + arr_datos[0] + ")")
        arr_monedas.append(arr_datos[0])
        arr_datos.pop(0)
    else:
        arr_turnos.append("Mateo agarra la ultima (" + arr_datos[len(arr_datos) - 1] + ")")
        arr_monedas.append(arr_datos[len(arr_datos) - 1])
        arr_datos.pop(len(arr_datos) - 1)


def pdinamica(arr_datos):
    cant_monedas = len(arr_datos)
    ganancia = [[0 for _ in range(cant_monedas)] for _ in range(cant_monedas)]
    # En el ejercicio "Caminos posibles de un laberinto", la ecuacion de recurrencia es:
    # Posibles[i][j] = Posibles[i-1][j] + Posibles[i][j-1]

    # (i-1 es haber venido de arriba, j-1 es haber venido de la izquierda)
    # En el ejercicio que le sigue, el laberinto pero con ganancias, en si es el mismo concepto, recorrer una matriz
    # ubicando la mayor ganancia al pasar pos las celdas, pero no nos dieron ecuacion de recurrencia... sospechoso.
    # En el siguiente a ese, es el anterior pero con obstaculos, nuevamente, sin ecuacionm de recurrencia.
    # Y si eso es equivalente a la segunda parte del TP? Siendo mateo los obstaculos, la primera moneda el caminar
    # hacia abajo, la ultima moneda el caminar hacia la derecha, recorrer una matriz, maximizando la ganancia.

    # Ecuacion de recurrencia que propongo:
    # OPT(i, j) = max   -> viene de arriba (agarro la primera):       V[i, j] + min(OPT(i-2, j), OPT(i-1, j-1))
    #                   -> viene de la izquierda (agarro la ultima):  V[i, j] + min(OPT(i, j-2), OPT(i-1, j-1))

    # min(OPT(i-2, j), OPT(i-1, j-1)) y min(OPT(i, j-2), OPT(i-1, j-1)) usa min porque Mateo manoteo la mas grande
    # entre las posibilidades anteriores al camino que tomo Sophia. El turno anterior era (i-1, j) si Sophia tomo la
    # primera o (i, j-1) si tomo la ultima.

    # Recordando que Mateo siempre agarra la mas grande en su turno:
    # OPT(i-2, j) es el turno de Sophia si agarro la primera, porque Mateo agarro la ultima (abajo, abajo)
    # OPT(i-1, j-1) es el turno de Sophia si agarro la primera, porque Mateo agarro la primera (abajo, derecha)
    # OPT(i, j-2) es el turno de Sophia si agarro la ultima, porque Mateo agarro la ultima (derecha, derecha)
    # OPT(i-1, j-1) es el turno de Sophia si agarro la ultima, porque Mateo agarro la primera (derecha, abajo)

    return ganancia


def obtener_lista_monedas(valores):
    return list(map(int, valores.split(";")))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            file = open(sys.argv[1], "rt")
            for line in file.read().splitlines():
                if not line.startswith("#"):
                    res = pdinamica(obtener_lista_monedas(line))
                    print(res)
                    break

            file.close()
        except IOError or OSError:
            print("Error al abrir el archivo")
            sys.exit()