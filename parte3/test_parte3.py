import parte3


modo = "BT"  # o "PL" o "JJ" o "AP"
res3_3_2 = parte3.elegir_algoritmo(parte3.obtener_datos("3_3_2.txt"), modo)
res5_5_6 = parte3.elegir_algoritmo(parte3.obtener_datos("5_5_6.txt"), modo)
res8_7_10 = parte3.elegir_algoritmo(parte3.obtener_datos("8_7_10.txt"), modo)
res10_3_3 = parte3.elegir_algoritmo(parte3.obtener_datos("10_3_3.txt"), modo)
res10_10_10 = parte3.elegir_algoritmo(parte3.obtener_datos("10_10_10.txt"), modo)
res12_12_21 = parte3.elegir_algoritmo(parte3.obtener_datos("12_12_21.txt"), modo)
res15_10_15 = parte3.elegir_algoritmo(parte3.obtener_datos("15_10_15.txt"), modo)
res20_20_20 = parte3.elegir_algoritmo(parte3.obtener_datos("20_20_20.txt"), modo)
res20_25_30 = parte3.elegir_algoritmo(parte3.obtener_datos("20_25_30.txt"), modo)
res30_25_25 = parte3.elegir_algoritmo(parte3.obtener_datos("30_25_25.txt"), modo)

assert res3_3_2[len(res3_3_2) - 2] == "Demanda cumplida: 4", res3_3_2[len(res3_3_2) - 2]
assert res5_5_6[len(res5_5_6) - 2] == "Demanda cumplida: 12", res5_5_6[len(res5_5_6) - 2]
assert res8_7_10[len(res8_7_10) - 2] == "Demanda cumplida: 26", res8_7_10[len(res8_7_10) - 2]
assert res10_3_3[len(res10_3_3) - 2] == "Demanda cumplida: 6", res10_3_3[len(res10_3_3) - 2]
assert res10_10_10[len(res10_10_10) - 2] == "Demanda cumplida: 40", res10_10_10[len(res10_10_10) - 2]
assert res12_12_21[len(res12_12_21) - 2] == "Demanda cumplida: 46", res12_12_21[len(res12_12_21) - 2]
assert res15_10_15[len(res15_10_15) - 2] == "Demanda cumplida: 40", res15_10_15[len(res15_10_15) - 2]
assert res20_20_20[len(res20_20_20) - 2] == "Demanda cumplida: 104", res20_20_20[len(res20_20_20) - 2]
assert res20_25_30[len(res20_25_30) - 2] == "Demanda cumplida: 172", res20_25_30[len(res20_25_30) - 2]
assert res30_25_25[len(res30_25_25) - 2] == "Demanda cumplida: 202", res30_25_25[len(res30_25_25) - 2]
