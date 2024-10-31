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
    tabla_ganancia = [0 for _ in range(cant_monedas)]
    """
    OPT(i, f) = max(V[i] + min(OPT(i + 1, f - 1), OPT(i + 2, f)), V[f] + min(OPT(i + 1, f - 1), OPT(i, f - 2)))
    
    i = indice primer valor del arreglo.
    f = indice ultimo valor del arreglo (len(V) - 1).
    max() = porque Sophia quiere maximizar su ganancia.
    V[i] = primer valor del arreglo, si lo toma, se pasa a (i + 1, f).
    V[j] = ultimo valor del arreglo, si lo toma, se pasa a (i, f - 1).
    min() = contemplar que Mateo se robo el max entre (i + 1, f) o (i, f - 1).
    OPT(i + 1, f - 1) = implica que Mateo se agarro el ultimo, V[f], posterior a Sophia agarrar el primero, V[i].
    OPT(i + 2, f) = implica que Mateo se agarro el primero, V[i], posterior a Sophia agarrar el primero, V[i].
    OPT(i + 1, f - 1) = implica que Mateo se agarro el primero, V[i], posterior a Sophia agarrar el ultimo, V[f].
    OPT(i, f - 2) = implica que Mateo se agarro el ultimo, V[f], posterior a Sophia agarrar el ultimo, V[i].
    
     ______________________________________________________________________________
    |-------------------------| Sophia agarra el primero | Sophia agarra el ultimo |
    | Mateo agarra el primero |      OPT(i + 2, f)       |    OPT(i + 1, f - 1)    |
    | Mateo agarra el ultimo  |     OPT(i + 1, f - 1)    |      OPT(i, f - 2)      |
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    
    Edit:
    Es estupido buscar el min() entre dos optimos cuando el objetivo es buscar el maximo valor obtenible posible.
    Queda mejor representado el que Mateo se agarre el primero o el ultimo usando una funcion partida:
    
    OPT(i, f) = max(V[i] + (OPT(i + 1, f - 1) si V[i+1] < V[f] else OPT(i + 2, f)),
                    V[f] + (OPT(i + 1, f - 1) si V[i] > V[f-1] else OPT(i, f - 2))
                    
    Yendo a la representacion, i es tanto el indice de inicio del arreglo como la fila, y f es el indice del fin del 
    arreglo tal cual es la columna. Mirar el seguimiento de la ecuacion de recurrencia del .xlsx. Las casillas azules 
    son los seguimientos de los optimos para esos dados (i, f), y cada valor de la tabla tambien lo es para cada tal.
    """

    return [0, 0, []]


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
