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


# Devuelve un array segun lo pedido en Resultados_Esperados.txt
def greedy(arr_datos):
    turnos = []
    monedas_sophia = []
    monedas_mateo = []

    i_primera = 0
    i_ultima = len(arr_datos) - 1
    turno_sophia = True
    while i_primera <= i_ultima:
        if turno_sophia:
            if arr_datos[i_primera] >= arr_datos[i_ultima]:
                turno("Primera moneda para Sophia", turnos, i_primera, monedas_sophia, arr_datos)
                i_primera += 1	
            else:
                turno("Última moneda para Sophia", turnos, i_ultima, monedas_sophia, arr_datos)
                i_ultima -= 1
        else:
            if arr_datos[i_primera] <= arr_datos[i_ultima]:
                turno("Primera moneda para Mateo", turnos, i_primera, monedas_mateo, arr_datos)
                i_primera += 1
            else:
                turno("Última moneda para Mateo", turnos, i_ultima, monedas_mateo, arr_datos)
                i_ultima -= 1
        turno_sophia = not turno_sophia


def obtener_lista_monedas(path):
    monedas = None
    try:
        file = open(path, "rt")
        for line in file.read().splitlines():
            if not line.startswith("#"):
                monedas = list(map(int, line.split(";")))
                break
        file.close()
    except IOError or OSError:
        print("Error al abrir el archivo")
        sys.exit()

    return monedas


if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = greedy(obtener_lista_monedas(sys.argv[1]))
        print(res[0], res[1], sep="\n")
