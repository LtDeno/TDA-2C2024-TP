import parte1


assert parte1.greedy(parte1.obtener_lista_monedas("20.txt"))[1] == "Ganancia de Sophia: " + str(7165)
assert parte1.greedy(parte1.obtener_lista_monedas("25.txt"))[1] == "Ganancia de Sophia: " + str(9635)
assert parte1.greedy(parte1.obtener_lista_monedas("50.txt"))[1] == "Ganancia de Sophia: " + str(17750)
assert parte1.greedy(parte1.obtener_lista_monedas("100.txt"))[1] == "Ganancia de Sophia: " + str(35009)
assert parte1.greedy(parte1.obtener_lista_monedas("1000.txt"))[1] == "Ganancia de Sophia: " + str(357814)
assert parte1.greedy(parte1.obtener_lista_monedas("10000.txt"))[1] == "Ganancia de Sophia: " + str(3550307)
assert parte1.greedy(parte1.obtener_lista_monedas("20000.txt"))[1] == "Ganancia de Sophia: " + str(7139357)
