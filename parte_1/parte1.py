import sys

'''
    La regla Greedy elegida acá es que Sophia se quede siempre con el mas grande entre ambas opciones, mientras que
    Mateo "jugando" se quede siempre con la mas chica entre ambas. El concepto es que Sophia no "vea" mas adelante en
    turnos que el actual, es decir, solo considera las 2 opciones que tiene, siendo asi que elije siempre la mayor,
    porque si mirase mas adelante, no buscaria un optimo local. Al mirar de tal forma al optimo local, ella elije
    siempre la moneda mas grande, dando siempre la mayor sumatoria para ella. Asimismo, como buena hermana que es,
    elije siempre la menor moneda para Mateo, para asegurarse que siempre le quede a ella la mayor moneda para su
    proximo turno. Es decir, busca un "in-optimo" / suboptimo / pésimo local para Mateo.

    O(n) porque se recorren todos los datos 1 vez.
    O(1) cada acceso al array, append e if.
    O(n) para los dos sum, O(n/2) para cada uno.
    O(n) final.
'''


def turno(indicacion, arr_turnos, indice, arr_monedas, arr_datos):
    arr_turnos.append(indicacion)
    arr_monedas.append(arr_datos[indice])
    arr_datos.pop(indice)


# Devuelve un array segun lo pedido en Resultados_Esperados.txt
def greedy(arr_datos):
    turnos = []
    monedas_sophia = []
    monedas_mateo = []
    turno_sophia = True

    while len(arr_datos) > 0:
        if turno_sophia:
            if arr_datos[0] > arr_datos[len(arr_datos) - 1]:
                turno("Primera moneda para Sophia", turnos, 0, monedas_sophia, arr_datos)
            else:
                turno("Última moneda para Sophia", turnos, len(arr_datos) - 1, monedas_sophia, arr_datos)
        else:
            if arr_datos[0] < arr_datos[len(arr_datos) - 1]:
                turno("Primera moneda para Mateo", turnos, 0, monedas_mateo, arr_datos)
            else:
                turno("Última moneda para Mateo", turnos, len(arr_datos) - 1, monedas_mateo, arr_datos)
        turno_sophia = not turno_sophia

    return [turnos, "Ganancia de Sophia: " + str(sum(monedas_sophia))]


def obtener_lista_monedas(valores):
    return list(map(int, valores.split(";")))


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            file = open(sys.argv[1], "rt")
            for line in file.read().splitlines():
                if not line.startswith("#"):
                    res = greedy(obtener_lista_monedas(line))
                    print(res[0], res[1], sep="\n")
                    break
            file.close()
        else:
            print(greedy([]))

    except IOError or OSError:
        print("Error al abrir el archivo")
        sys.exit()
