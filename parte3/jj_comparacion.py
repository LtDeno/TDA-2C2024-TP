import parte3


algoritmo_optimo = "BT"  # o "PL"
casos_de_prueba = ["3_3_2.txt", "5_5_6.txt", "8_7_10.txt", "10_3_3.txt", "10_10_10.txt", "12_12_21.txt", "15_10_15.txt", "20_20_20.txt"]

with open(f"jj_posibles_cotas_empiricas.txt", "w") as archivo_resultados:
    for archivo in casos_de_prueba:
        res_OPT = parte3.elegir_algoritmo_demanda_cumplida(parte3.obtener_datos(archivo), algoritmo_optimo)
        res_JJ = parte3.elegir_algoritmo_demanda_cumplida(parte3.obtener_datos(archivo), "JJ")
        archivo_resultados.write(f"I={archivo}, z(I)= {res_OPT}, A(I) = {res_JJ}, A(I)/z(I) = {(res_JJ/res_OPT)}\n")