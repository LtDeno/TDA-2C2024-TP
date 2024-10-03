from time import time

import parte1


def abrir_datos(path):
    file = open(path, "rt")
    datos = []
    for line in file.read().splitlines():
        if not line.startswith("#"):
            datos = parte1.obtener_lista_monedas(line)
            break
    file.close()
    return datos


def iterar_datos(path):
    datos = abrir_datos(path)
    for dato in datos:
        dato = 0


assert parte1.greedy(abrir_datos("20.txt"))[0] == 7165
assert parte1.greedy(abrir_datos("25.txt"))[0] == 9635
assert parte1.greedy(abrir_datos("50.txt"))[0] == 17750
assert parte1.greedy(abrir_datos("100.txt"))[0] == 35009
assert parte1.greedy(abrir_datos("1000.txt"))[0] == 357814
assert parte1.greedy(abrir_datos("10000.txt"))[0] == 3550307
assert parte1.greedy(abrir_datos("20000.txt"))[0] == 7139357

if __name__ == '__main__':
    start1 = time()
    iterar_datos("20000.txt")
    end1 = time()
    print(f"Duracion de recorrer los datos: {end1 - start1} segundos")

    start2 = time()
    parte1.greedy(abrir_datos("20000.txt"))
    end2 = time()
    print(f"Duracion de recorrer los datos: {end2 - start2} segundos")
