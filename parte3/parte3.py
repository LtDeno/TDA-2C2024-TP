import sys, bt, pl, jj, ap


"""
1) Demostrar que el Problema de la Batalla Naval se encuentra en NP: 
        Un problema NP es aquel problema para el que existe un certificador eficiente, es decir, que se puede validar 
    en  tiempo polinomial. 
        Para demostrar que el Problema de la Batalla Naval se encuentra en NP, se debe proponer un certificador que 
    valide su resultado en tiempo polinomial (no tiene que resolverlo, solo validar lo que devolvio). En este caso, 
    devuelve un tablero, que para validarlo se pueden recorrer todas sus casillas en O(n x m), disminuyendo en 1 los 
    valores de demanda, en sus respectivos indices, en las listas de fila y columna, si la casilla que se esta
    recorriendo esta ocupada. Terminado el recorrido de todo el tablero, se hace la sumatoria de ambas listas, que 
    quedarian siendo las demandas de fila y columna  insatisfechas, en O(n) y O(m) respectivamente, dando como 
    resultado a la validacion la cantidad de demandas insatisfechas. Esta comprobacion tambien puede devolver, digamos,
    -1 como flag para informar que hubo al menos una fila o columna en la cual se ocuparon demasiados casilleros (mas
    que lo pedido por la demanda).
        La previa demostracion no es exclusiva, implicando que pueden haber otros validadores (y asi demostraciones)
    para el Problema de la Batalla Naval. Otro ejemplo de un validador puede ser validar la cantidad de barcos colocados
    en las filas, tal se usaria en la demostracion siguiente.
       
2) Demostrar que el Problema de la Batalla Naval es un problema NP-Completo:
        Un problema NP-Completo es aquel que se encuentra en NP y, al mismo tiempo, todos los problemas NP pueden 
    reducirse a el. En criollo, NP-Completo son problemas very difficult.
        Si un problema NP-Completo puede reducirse a un problema X, entonces, dicho problema X es NP-Completo, por
    propiedad de transitividad.
        Para demostrar que el Problema de la Batalla Naval es un problema NP-Completo, se necesita reducir un problema 
    Y NP-Completo, que se pueda demostrar (sea porque se vio en clase como tal o porque sin trampa se puede demostrar),
    al problema X de la Batalla Naval.
        ~sujeto a modificacion para otra propuesta~
        Se propone reducir el problema de Independent Set (demostrada NP-Completitud en clase) al problema de la
    Batalla Naval.
        Por parte del Independent Set, se tiene un grafo como parametro, con vertices, aristas y metodos (concretamente 
    grafo.obtener_vertices() y grafo.adyacentes(vertice)), siendo N la cantidad de vertices de dicho grafo. Tambien se
    posee de un valor K, donde el problema implica devolver True si la existe un Independent Set de al menos k verices.
    Por parte de Batalla Naval, se tiene un tablero, un array de barcos, un array de demandas de filas y un array de 
    demandas de columnas. Para reducirlo se propone:
        - un tablero de dimensiones NxN;
        - un arreglo de N barcos, donde cada i (es decir, cada longitud de barco) sea la cantidad de adyacentes al 
        vertice i.
        - un arreglo de demandas de filas, donde cada j (es decir, cada demanda de fila) sea la cantidad de adyacentes
        al vertice j. Si, es lo mismo que el arreglo de barcos;
        - un arreglo de demandas de columnas, donde cada j (es decir, cada demanda de columa) sea un numero muy grande,
        de manera tal que no se lograse satisfacer. Dicho numero muy grande puede ser tanto infinito como V+1. 
        La longitud de este arreglo es, nuevamente, N.
    Esto resulta en el tablero con la mayor cantidad de barcos colocados, luego se precisa de un validador (eficiente y 
    que valide en tiempo polinomial) para saber cuantos barcos colocados hay. Cada barco es un vertice contenido en el 
    Independent set. Como ultimo, se compara esa cantidad de barcos colocados al valor K, devolviendose True si hay al
    menos K barcos (vertices) en el tablero (el Independent Set).
        Fuese otro el requisito del problema de Independent Set, como, por ejemplo, obtener dicho set, se podria armar
    un set con los barcos ubicados en el tablero, que son, propiamente, los vertices en el set.
        El Problema de la Batalla Naval es un problema NP-Completo.
                                                                                                quod erat demonstrandum
"""


# Devuelve la demanda insatisfecha/restante
def calcular_demanda_cumplida(asignaciones):
    suma = 0
    for asignacion in asignaciones.values():
        suma += (abs(asignacion[0][0] - asignacion[1][0]) + abs(asignacion[0][1] - asignacion[1][1]) + 1) * 2
    return suma


# Crea un formato segun Resultados_Esperados.txt
def formatear_resultados(asignaciones, d_total):
    formateado = ["Posiciones:"]
    for key in asignaciones.keys():
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
