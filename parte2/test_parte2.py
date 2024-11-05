import parte2


res5 = parte2.pdinamica(parte2.obtener_lista_monedas("5.txt"))
res10 = parte2.pdinamica(parte2.obtener_lista_monedas("10.txt"))
res20 = parte2.pdinamica(parte2.obtener_lista_monedas("20.txt"))
res25 = parte2.pdinamica(parte2.obtener_lista_monedas("25.txt"))
res50 = parte2.pdinamica(parte2.obtener_lista_monedas("50.txt"))
res100 = parte2.pdinamica(parte2.obtener_lista_monedas("100.txt"))
res1000 = parte2.pdinamica(parte2.obtener_lista_monedas("1000.txt"))
res2000 = parte2.pdinamica(parte2.obtener_lista_monedas("2000.txt"))
res5000 = parte2.pdinamica(parte2.obtener_lista_monedas("5000.txt"))
res10000 = parte2.pdinamica(parte2.obtener_lista_monedas("10000.txt"))

# Sophiaabrir_datos
assert res5[1] == "Ganancia Sophia: " + str(1483)
assert res10[1] == "Ganancia Sophia: " + str(2338)
assert res20[1] == "Ganancia Sophia: " + str(5234)
assert res25[1] == "Ganancia Sophia: " + str(7491)
assert res50[1] == "Ganancia Sophia: " + str(14976)
assert res100[1] == "Ganancia Sophia: " + str(28844)
assert res1000[1] == "Ganancia Sophia: " + str(1401590)
assert res2000[1] == "Ganancia Sophia: " + str(2869340)
assert res5000[1] == "Ganancia Sophia: " + str(9939221)
assert res10000[1] == "Ganancia Sophia: " + str(34107537)

# Mateo
assert res5[2] == "Ganancia Mateo: " + str(1268)
assert res10[2] == "Ganancia Mateo: " + str(1780)
assert res20[2] == "Ganancia Mateo: " + str(4264)
assert res25[2] == "Ganancia Mateo: " + str(6523)
assert res50[2] == "Ganancia Mateo: " + str(13449)
assert res100[2] == "Ganancia Mateo: " + str(22095)
assert res1000[2] == "Ganancia Mateo: " + str(1044067)
assert res2000[2] == "Ganancia Mateo: " + str(2155520)
assert res5000[2] == "Ganancia Mateo: " + str(7617856)
assert res10000[2] == "Ganancia Mateo: " + str(25730392)
