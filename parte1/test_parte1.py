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


assert parte1.greedy(abrir_datos("20.txt"))[1] == "Ganancia de Sophia: " + str(7165)
assert parte1.greedy(abrir_datos("25.txt"))[1] == "Ganancia de Sophia: " + str(9635)
assert parte1.greedy(abrir_datos("50.txt"))[1] == "Ganancia de Sophia: " + str(17750)
assert parte1.greedy(abrir_datos("100.txt"))[1] == "Ganancia de Sophia: " + str(35009)
assert parte1.greedy(abrir_datos("1000.txt"))[1] == "Ganancia de Sophia: " + str(357814)
assert parte1.greedy(abrir_datos("10000.txt"))[1] == "Ganancia de Sophia: " + str(3550307)
assert parte1.greedy(abrir_datos("20000.txt"))[1] == "Ganancia de Sophia: " + str(7139357)
