import sys

"""
    OPT(i, f) = max(V[i] + (OPT(i + 1, f - 1) si V[i+1] < V[f] sino OPT(i + 2, f)),
                    V[f] + (OPT(i + 1, f - 1) si V[i] > V[f-1] sino OPT(i, f - 2))
    
    i = indice primer valor del arreglo.
    f = indice ultimo valor del arreglo (len(V) - 1).
    max() = porque Sophia quiere maximizar su ganancia.
    V[i] = primer valor del arreglo, si lo toma, se pasa a (i + 1, f).
    V[j] = ultimo valor del arreglo, si lo toma, se pasa a (i, f - 1).
    OPT(i + 1, f - 1) = implica que Mateo se agarro el ultimo, V[f], posterior a Sophia agarrar el primero, V[i].
    OPT(i + 2, f) = implica que Mateo se agarro el primero, V[i], posterior a Sophia agarrar el primero, V[i].
    OPT(i + 1, f - 1) = implica que Mateo se agarro el primero, V[i], posterior a Sophia agarrar el ultimo, V[f].
    OPT(i, f - 2) = implica que Mateo se agarro el ultimo, V[f], posterior a Sophia agarrar el ultimo, V[i].
    
     ______________________________________________________________________________
    |-------------------------| Sophia agarra el primero | Sophia agarra el ultimo |
    | Mateo agarra el primero |      OPT(i + 2, f)       |    OPT(i + 1, f - 1)    |
    | Mateo agarra el ultimo  |     OPT(i + 1, f - 1)    |      OPT(i, f - 2)      |
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
     
    Yendo a la representacion, i es tanto el indice de inicio del arreglo como la fila, y f es el indice del fin del 
    arreglo tal cual es la columna. Mirar el seguimiento de la ecuacion de recurrencia del .xlsx. Las casillas azules 
    son los seguimientos de los optimos para esos dados (i, f), y cada valor de la tabla tambien lo es para cada tal.
    
    Induccion matematica:
    1) Planteo casos base:
        i = 0      -> OPT(0, 0) = 0 es optimo y el valor maximo porque no hay valores;
        i = f      -> OPT(i, i) = V[i] es optimo y el valor maximo porque hay un solo valor, siendo ese el maximo;
        i = f - 1  -> OPT(i, i+1) = max(V[i], V[i+1]) es optimo y el valor maximo porque, dado un solo turno, se elije
                                                      el valor mas alto entre ambos.
    2) Paso inductivo: 
        OPT(i, f) = max(V[i] + (OPT(i + 1, f - 1) si V[i+1] < V[f] sino OPT(i + 2, f)),
                        V[f] + (OPT(i + 1, f - 1) si V[i] > V[f-1] sino OPT(i, f - 2))
        3 posibilidades para el llamado recursivo:
         - OPT(i + 1, f - 1);
         - OPT(i + 2, f);
         - OPT(i, f - 2)
        posibilidades, hipotesis, las cuales suponemos verdaderas. Se repiten asi los llamados recursivos con las 3 
        posibilidades hasta llegar a alguno de los casos base planteados, casos ya antes demostrados como optimos,
        dejando asi demostrado OPT(i, f) como optimo.
"""


def texto(jugador, posicion, valor):
    return jugador + " debe agarrar la " + posicion + " (" + str(valor) + ")"


def reconstruccion(monedas, tabla):
    sum_sophia = 0
    sum_mateo = 0
    turnos = []
    i = 0
    f = len(monedas) - 1
    turno_sophia = True

    while f >= i:
        if turno_sophia:
            i_aux_primera_moneda = (i + 1) if monedas[i + 1] < monedas[f] else (i + 2)
            f_aux_primera_moneda = (f - 1) if monedas[i + 1] < monedas[f] else f
            i_aux_ultima_moneda = (i + 1) if monedas[i] > monedas[f - 1] else i
            f_aux_ultima_moneda = (f - 1) if monedas[i] > monedas[f - 1] else (f - 2)

            if (monedas[f] + tabla[i_aux_ultima_moneda][f_aux_ultima_moneda] >
                    monedas[i] + tabla[i_aux_primera_moneda][f_aux_primera_moneda]):
                sum_sophia += monedas[f]
                turnos.append(texto("Sophia", "ultima", monedas[f]))
                f -= 1
            else:
                sum_sophia += monedas[i]
                turnos.append(texto("Sophia", "primera", monedas[i]))
                i += 1

        else:
            if monedas[f] >= monedas[i]:
                sum_mateo += monedas[f]
                turnos.append(texto("Mateo", "ultima", monedas[f]))
                f -= 1
            else:
                sum_mateo += monedas[i]
                turnos.append(texto("Mateo", "primera", monedas[i]))
                i += 1

        turno_sophia = not turno_sophia

    return [turnos, "Ganancia Sophia: " + str(sum_sophia), "Ganancia Mateo: " + str(sum_mateo)]


# Devuelve un array segun lo pedido en Resultados_Esperados.txt
def pdinamica(monedas):
    cant_monedas = len(monedas)
    tabla = [[0 for _ in range(cant_monedas)] for _ in range(cant_monedas)]

    for indice in range(cant_monedas):
        tabla[indice][indice] = monedas[indice]
        if indice < cant_monedas - 1:
            tabla[indice][indice + 1] = max(monedas[indice], monedas[indice + 1])

    for j in range(2, cant_monedas):
        for i in range(cant_monedas - j):
            f = i + j
            tabla[i][f] = max(monedas[i] + (tabla[i + 1][f - 1] if monedas[i + 1] < monedas[f] else tabla[i + 2][f]),
                              monedas[f] + (tabla[i + 1][f - 1] if monedas[i] > monedas[f - 1] else tabla[i][f - 2]))

    return reconstruccion(monedas, tabla)


def obtener_lista_monedas(valores):
    return list(map(int, valores.split(";")))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            file = open(sys.argv[1], "rt")
            for line in file.read().splitlines():
                if not line.startswith("#"):
                    res = pdinamica(obtener_lista_monedas(line))
                    print(res[0], res[1], res[2], sep="\n")
                    break

            file.close()
        except IOError or OSError:
            print("Error al abrir el archivo")
            sys.exit()