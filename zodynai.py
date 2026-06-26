# # sarasas = [2,2,5,3,5,1,7,3,6,11,2,5,4,5,3]
# # zodynas = {}
 
# # for skaicius in sarasas:
# #     if zodynas.get(skaicius) == None: # jei tokio rakto nera
# #         zodynas[skaicius] = 1 # priskiriame reiksme 1
# #     else:
# #         zodynas[skaicius] += 1 # jeigu raktas egzistuoja, pridedame 1 prie esamos reiksmes

# # # atspausdinti didziausia reiksme is zodyno

# # # first_key = list(zodynas.keys())[0]
# # # max_raktas = first_key
# # # max_reiksme = zodynas[first_key]

# # # for raktas in zodynas:
# # #     if zodynas[raktas] > max_reiksme:
# # #         max_reiksme = zodynas[raktas]
# # #         max_raktas = raktas

# # # print(f"Daugiausiai pasikartojantis skaicius yra {max_raktas}, pasikartojantis {max_reiksme} kartus")


# # # first_key = list(zodynas.keys())[0]
# # # max_raktas = first_key
# # max_reiksme = 0

# # for raktas in zodynas:
# #     if zodynas[raktas] > max_reiksme:
# #         max_reiksme = zodynas[raktas]
# #         max_raktas = raktas

# # print(f"Daugiausiai pasikartojantis skaicius yra {max_raktas}, pasikartojantis {max_reiksme} kartus")

# # zodynas = {
# #     "vardas": "Justas",
# #     "amzius": 25,
# #     "miestas": "Vilnius"
# # }
# # # list(zodynas.keys())
# # print(zodynas.keys()) # grazina visus raktus
# # print(list(zodynas.keys())) # grazina pirma rakta
# # int("F")

# # print(range(0,10, 2)) # range(start, stop, step)

# # for


# # in
# # for i in range(0,10,2):
# #     print(i)

# # sarasas = [2,2,5,3,5,1,7,3,6,11,2,5,4,5,3]

# # if 19 in sarasas: # in galim naudoti, noredami patikrinti ar sarase yra tam tikra reiksme
# #     print("Yra")

# # zodynas = {
# #     "vardas": "Justas",
# #     "amzius": 25,
# #     "miestas": "Vilnius"
# # }
# # if "amzius" in zodynas: # in galim naudoti, noredami patikrinti ar zodyne yra tam tikras raktas
# #     print("Yra")

# # tuple (list ir dictionary)

# # sarasas = [2,2,5,3,5,1,7,3,6,11,2,5,4,5,3] # list yra pasiekiamas (mutable)
# # tuplas = (2,2,5,3,5,1,7,3,6,11,2,5,4,5,3) # tuple yra nepasiekiamas (immutable)

# # sarasas.append(100)

# # tuplas.append(100) # tuple negalima keisti, prideti, pasalinti elementu

# # print(tuplas[0])
# # tuplas[0]  = 100 # tuple negalima keisti, prideti, pasalinti elementu

# # tuplas = (2,3) 

# # a, b, c = tuplas # tuple galima isiskleisti i kintamuosius (unpacking)
# # print(a)
# # print(b)

# # zodynas = {
# #     "vardas": "Justas",
# #     "amzius": 25,
# #     "miestas": "Vilnius"
# # }
# # # print(zodynas.items())

# # for pora in zodynas.items(): # items grazina poras (raktas, reiksme)

# #     print(f"Raktas: {pora[0]}, reiksme: {pora[1]}")

# # for raktas, reiksme in zodynas.items(): # raktas, reiksme =  zodynas.items[0]
# #     print(f"Raktas: {raktas}, reiksme: {reiksme}")

# # zodynas = {
# #     "vardas": "Justas",
# #     "amzius": 25,
# #     "miestas": "Vilnius"
# # }


# # # update
# # zodynas.update({"amzius": 26, "salys": "Lietuva"}) # update pakeicia esama reiksme arba prideda nauja
# # print(zodynas)

# # zodynas = {"Azuolas":20, "Jonas":39, "Mantas":18}
 
# # first_key = list(zodynas.keys())[0]
# # min_raktas = first_key
# # min_reiksme = zodynas[first_key]
 
# # for rakt, reiksm in zodynas.items(): # pora | rakt, reiksm = pora
# #     if reiksm < min_reiksme:
# #         min_r1eiksme = reiksm
# #         min_raktas = rakt

# # print(min_raktas)

# # import random # library/biblioteka

# # atsitiktinis = random.randint(1,5)
# # print(atsitiktinis)

# import random as rd # alias

# atsitiktinis = rd.randint(1,5)

# print(atsitiktinis)

# # print(random.randint(1, 100)) 

# kint = 5
# print(kint)
# print(kint+7)
# print(kint)
# kint = kint + 7
# print(kint)

import datetime as dt

# print(dt.date.today())
# siandien = dt.date.today()

# mano_gimtadienis = dt.date(1998, 5, 12)
# print(mano_gimtadienis)
# # let's calculate the age
# # amzius = siandien.year - mano_gimtadienis.year

# # print(amzius)
# print(siandien.year)
# print(siandien.month)
# print(siandien.day)

# skirtumas = (siandien - mano_gimtadienis)

# # calculate age
# amzius = skirtumas.days // 365 # // - dalyba be liekanos
# print(amzius)

# metai = int(input("Iveskite savo gimimo metus: "))
# menuo = int(input("Iveskite savo gimimo menesi: "))
# diena = int(input("Iveskite savo gimimo diena: "))
# mano_gimtadienis = dt.date(metai, menuo, diena)

# siandien = dt.date.today()

# skirtumas = (siandien - mano_gimtadienis)
# amzius = skirtumas.days // 365
# print(f"Jusu amzius yra {amzius} metai(-u)")

# date from one input
# data_string = input("Iveskite savo gimimo data (YYYY-MM-DD): ")
# print(data_string)
# data_date = dt.datetime.strptime(data_string, "%Y-%m-%d").date() # strptime - string parse time
# print(data_date)


# date_string_foatted = data_date.strftime("%Y/%B/%d %A") # strftime - string format time
# print(date_string_foatted)
dt.datetime(2024, 6, 14, 15, 30, 45) # datetime(year, month, day, hour, minute, second)


# if (siandien.month, siandien.day) < (mano_gimtadienis.month, mano_gimtadienis.day):
#     amzius -= 1