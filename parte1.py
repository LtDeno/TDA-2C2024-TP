import sys


def greedy(datos):
    print(datos)


def obtener_lista_monedas(valores):
    return list(map(int, valores.split(";")))


if __name__ == "__main__":
    try:
        file = open(sys.argv[1], "rt")
        for line in file.read().splitlines():
            if not line.startswith("#"):
                greedy(obtener_lista_monedas(line))
                break

        file.close()
    except IOError or OSError:
        print("Error al abrir el archivo")
        sys.exit()

