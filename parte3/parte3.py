import sys, bt, pl, jj, ap


# Devuelve la demanda insatisfecha/restante
def calcular_demanda_cumplida(asignaciones):
    suma = 0
    for asignacion in asignaciones.values():
        if asignacion is not None:
            suma += (abs(asignacion[0][0] - asignacion[1][0]) + abs(asignacion[0][1] - asignacion[1][1]) + 1) * 2
    return suma


# Crea un formato segun Resultados_Esperados.txt
def formatear_resultados(asignaciones, d_total):
    formateado = ["Posiciones:"]
    for key in asignaciones.keys():
        if asignaciones[key] is None:
            formateado.append(str(key) + ": " + str(asignaciones[key]))
        else:
            formateado.append(str(key) + ": " + str(asignaciones[key][0]) + " - " + str(asignaciones[key][1]))

    formateado.append("Demanda cumplida: " + str(calcular_demanda_cumplida(asignaciones)))
    formateado.append("Demanda total: " + str(d_total))
    return formateado


def gen_asignacion(fila_fin, fila_inicio, columna_fin, columna_inicio):
    return [(fila_fin, columna_fin), (fila_inicio, columna_inicio)]


# Elije el algoritmo segun el argumento de ejecucion del programa, usa por defecto Backtracking.
# El algoritmo devuelve la asignacion de posiciones, y ya que estamos,
# coloca los barcos en el tablero para que el validador lo valide.
# Las asignaciones, en un diccionario, han de ser ordenadas segun el orden en el arreglo de barcos y generadas usando gen_asignacion().
def elegir_algoritmo(datos, modo):
    tablero = [[0 for _ in range(len(datos[2]))] for _ in range(len(datos[1]))]
    asignaciones = None

    if modo == "PL":
        asignaciones = pl.proglineal(tablero, datos[0], datos[1], datos[2])
    elif modo == "JJ":
        asignaciones = jj.johnjellicoe(tablero, datos[0], datos[1], datos[2])
    elif modo == "AP":
        asignaciones = ap.aproximacion(tablero, datos[0], datos[1], datos[2])
    else:
        asignaciones = bt.backtracking(tablero, datos[0], datos[1], datos[2])

    return formatear_resultados(asignaciones, sum(datos[1]) + sum(datos[2]))


def elegir_algoritmo_demanda_cumplida(datos, modo):
    tablero = [[0 for _ in range(len(datos[2]))] for _ in range(len(datos[1]))]
    asignaciones = None

    if modo == "PL":
        asignaciones = pl.proglineal(tablero, datos[0], datos[1], datos[2])
    elif modo == "JJ":
        asignaciones = jj.johnjellicoe(tablero, datos[0], datos[1], datos[2])
    elif modo == "AP":
        asignaciones = ap.aproximacion(tablero, datos[0], datos[1], datos[2])
    else:
        asignaciones = bt.backtracking(tablero, datos[0], datos[1], datos[2])

    return calcular_demanda_cumplida(asignaciones)


# Devuelve un array con, y en este orden: array de barcos, array de demanda de filas y array de demanda de columnas.
def obtener_datos(path):
    try:
        file = open(path, "rt")
        f_data = file.read().splitlines()
        file.close()

        datos = {0: [], 1: [], 2: []}
        algun_contador = 0
        for line in f_data:
            if not line.startswith("#"):
                if line.strip("") == "":
                    algun_contador += 1
                    continue
                datos[algun_contador].append(int(line))
        return [datos[2], datos[0], datos[1]]

    except IOError or OSError:
        print("Error al abrir el archivo")
        sys.exit()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        datos_formateados = obtener_datos(sys.argv[1])
        resultado = None

        if len(sys.argv) > 2:
            resultado = elegir_algoritmo(datos_formateados, sys.argv[2])
        else:
            resultado = elegir_algoritmo(datos_formateados, "BT")

        for res in resultado:
            print(res)
