from time import time
import parte2


def abrir_datos(path):
    file = open(path, "rt")
    datos = []
    for line in file.read().splitlines():
        if not line.startswith("#"):
            datos = parte2.obtener_lista_monedas(line)
            break
    file.close()
    return datos


# Sophiaabrir_datos
assert parte2.pdinamica(abrir_datos("5.txt"))[0] == 1483
assert parte2.pdinamica(abrir_datos("10.txt"))[0] == 2338
assert parte2.pdinamica(abrir_datos("20.txt"))[0] == 5234
assert parte2.pdinamica(abrir_datos("25.txt"))[0] == 7491
assert parte2.pdinamica(abrir_datos("50.txt"))[0] == 14976
assert parte2.pdinamica(abrir_datos("100.txt"))[0] == 28844
assert parte2.pdinamica(abrir_datos("1000.txt"))[0] == 1401590
assert parte2.pdinamica(abrir_datos("2000.txt"))[0] == 2869340
assert parte2.pdinamica(abrir_datos("5000.txt"))[0] == 9939221
assert parte2.pdinamica(abrir_datos("10000.txt"))[0] == 34107537

# Mateo
assert parte2.pdinamica(abrir_datos("5.txt"))[1] == 1268
assert parte2.pdinamica(abrir_datos("10.txt"))[1] == 1780
assert parte2.pdinamica(abrir_datos("20.txt"))[1] == 4264
assert parte2.pdinamica(abrir_datos("25.txt"))[1] == 6523
assert parte2.pdinamica(abrir_datos("50.txt"))[1] == 13449
assert parte2.pdinamica(abrir_datos("100.txt"))[1] == 22095
assert parte2.pdinamica(abrir_datos("1000.txt"))[1] == 1044067
assert parte2.pdinamica(abrir_datos("2000.txt"))[1] == 2155520
assert parte2.pdinamica(abrir_datos("5000.txt"))[1] == 7617856
assert parte2.pdinamica(abrir_datos("10000.txt"))[1] == 25730392
