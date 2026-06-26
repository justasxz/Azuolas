# if # jeigu sitas tiesa
# tuomet daryk sita
# else # kitu atveju
# daryk sita

# amzius = 101
# if amzius < 18: # patikrina sita, jeigu ne tiesa tik tada eina i elifa
#     print("Tu esi nepilnametis")
# elif amzius < 65: # sitas tikrinamas tik atuo atveju jeigu pirmas ifas nebuvo tiesa
#     print("Tu esi suauges")
# elif amzius < 100: # sitas tikrinamas tik atuo atveju jeigu pirmas ifas nebuvo tiesa
#     print("Tu esi pensininkas")
# else:
#     print("Tu esi simtametis")
# amzius = 5
# if amzius < 18: # patikrina sita, jeigu ne tiesa tik tada eina i elifa
#     print("Tu esi nepilnametis")
# if amzius < 65: # sitas tikrinamas tik atuo atveju jeigu pirmas ifas nebuvo tiesa
#     print("Tu esi suauges")
# if amzius < 100: # sitas tikrinamas tik atuo atveju jeigu pirmas ifas nebuvo tiesa
#     print("Tu esi pensininkas")
# else:
#     print("Tu esi simtametis")

# amzius = 17
# vidurkis = 9.5

# if amzius >= 18 and vidurkis >= 8: # True + True
#     print("Tu gali stoti i universitetus")
# else:
#     print("Tu negali stoti i universitetus")

# print("Programa baigta")

# amzius = 15
# su_tevais = True

# if amzius >= 16 or su_tevais == True: # False + True
#     print("Tu gali eiti i siaubo filma")
# else:
#     print("Tu negali eiti i siaubo filma")
# print("Programa baigta")

# sarasas = [7, -9, 52, 0] # list/array
# # print(sarasas)
# sarasas2 = ["Zodis", 5, -3.5, True]
# # print(sarasas2)
# # sarasas3 = [] # tuscias sarasas
# # print(sarasas3)
# # sarasas3.append(19)
# # sarasas3.append(19)
# # sarasas3.append(19)
# # print(sarasas3)
# print(sarasas[0])
# sarasas[1] = sarasas[1] * sarasas[1] # saraso 1 vieta (nuo nulio) nuo siol bus saraso 1 elementas kart 1 elementas
# print(sarasas)
# sarasas.pop(2)
# print(sarasas)

# ciklas

# sarasas = [7, -9, 52, 0]

# for skaicius in sarasas: # skaicius = sarasas[0], skaicius = sarasas[1], skaicius = sarasas[2], skaicius = sarasas[3]
#     print(skaicius)
#     print("Pasibaige vienas ciklas")

# islaidos = [20,15,30,19,7,4,9,2,5,7,6,5,5,8,4,3,2,1]

# # for islaida in islaidos: # islaida = islaidos[0], islaida = islaidos[1], ...
# #     print(f"Siandien isleista: {islaida} eur")


# suma = 0

# for islaida in islaidos: # islaida = islaidos[0], islaida = islaidos[1], ...
#     suma = suma + islaida

# print(f"Is viso islaidos: {suma}")
# print(round(suma / len(islaidos), 3)) # suapvalina iki 2 skaiciu po kablelio
# ar per menesi buvo dienu, kai isleista daugiau nei 50 eur
# islaidos = [20,15,51,30,19,7,4,9,2,52,7,6,5,5,8,4,3,2,1]

# for islaida in islaidos:
#     if islaida > 50:
#         print("Buvo dienu kai isleista daugiau nei 50 eur")
#         break # nutraukia cikla
# print("Programa baigta")
# sarasas = list(range(50)) # [0,1,2,3,...49] (paskutinis skaicius nera imamas)

# # print(sarasas)

# for skaicius in sarasas:
#     print(skaicius)

# sarasas = range(15,50) # [15,16,17...49] (paskutinis skaicius nera imamas)


# for skaicius in sarasas:
#     print(skaicius)

# sarasas = range(15,50,2) # [15,17,19...49] (paskutinis skaicius nera imamas)


# for skaicius in sarasas:
#     print(skaicius)
# range(start, stop, step)
# print(list(range(100,10,-3))) # nuo 0 iki 100 kas 5

# sarasas = range(1,10000000)

# for _ in sarasas: # _ kintamojo pavadinimas, kai kintamasis nenaudojamas
#     ivestis = input("Iveskite skaiciu (q - iseiti): ")
#     print(ivestis)
#     if ivestis == "q":
#         break
# print("Programa baigta")

# for ciklas - eina per visus saraso elementus
# kint = 0

# while 2>0:
#     # print("Ciklas veikia")
#     kint = kint + 1
#     print(kint)
#     if kint == 10:
#         break

# limitas = 5
# kint = 0

# while kint < limitas: # kol kint yra mazesnis uz limita
#     kint = kint + 1
#     print(kint)


# sarasas = [5,3,2]
# suma = 0
# for skaicius in sarasas: # skaicius = 5
#     suma = suma + skaicius # suma = 0 + 5 | suma = 5 + 3 | suma = 8 + 2

# print(suma)