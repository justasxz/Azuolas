# pazymiai = {"Jonas": [10, 8, 6, 4], "Ona": [9, 7, 5, 3], "Petras": [8, 6, 4, 2]}

# # sarasas = [1,2,3,4,5,6]
# sarasas2 = [[1,2,3], [4,5,6], [7,8,9]] # sarasas sarasu

# print(sarasas2[0][0])
# naujas = sarasas2[0]
# print(naujas)

# zmoniu_daiktai = {
#     "Jonas": {"automobilis":"Toyota", "namas":"Prestiziskas"},
#     "Ona": {"automobilis":"BMW", "namas":"Namas prie juros"},
#     "Petras": {"automobilis":"Audi", "namas":"Namas prie ezeru"}
# }

# print(zmoniu_daiktai["Jonas"])


# pazymiai = {"Jonas": [10, 8, 6, 4], "Ona": [9, 7, 3], "Petras": [8, 6]}

# for zmogus in pazymiai.items():
#     print(zmogus[0])
#     suma = 0
#     #print(zmogus[1])
#     for pazymis in zmogus[1]:
#         print(pazymis)
#         suma = suma + pazymis
#     print(suma)
#     #Cia baigesi vienas zmogus


# funkcijos 

# def pasisveikink(): # funkcija (zinom, kad funkcija, nes yra zodis def) o funkcijos pavadinimas pasisveikink
#     print("Labas")
#     print("Kaip sekasi?")
#     print("Viso gero")

# pasisveikink() # funkcijos iskvietimas (kad funkcija butu ivykdyta, reikia ja iskviesti)
# pasisveikink() # funkcijos iskvietimas (kad funkcija butu ivykdyta, reikia ja iskviesti)
# pasisveikink() # funkcijos iskvietimas (kad funkcija butu ivykdyta, reikia ja iskviesti)
# pasisveikink() # funkcijos iskvietimas (kad funkcija butu ivykdyta, reikia ja iskviesti)

# sarasas = [1,2,3,4,5]

# def sudek_skaicius():
#     skaicius1 = 10
#     skaicius2 = 20
#     suma = skaicius1 + skaicius2
#     # print(suma)
#     return suma


# # sudek_skaicius() # funkcijos rezultatas pagal nutylejima yra None
# # vietoje funkcijos iskvietimo (o iskvietimas yra pavadinimas()) mes gauname funkcijos rezultata
# print(sudek_skaicius())
# print(sudek_skaicius() /2)

# print(sudek_skaicius())

# def grazink_5():
#     return 5

# print(grazink_5())
# def grazink_varda():
#     return "Justas"

# print(f"Grazintas vardas yra {grazink_varda()}")


# def skaiciai():
#     if False:
#         return [1,2,3,4,5]
#     else:
#         return [6,7,8,9,10] # grazinam visais atvejais, neturetu buti atveju kai negrazinama, jeigu bent kazkas yra grazinama


# print(skaiciai())


# grazinta_reiksme = skaiciai()

# print(sarasas)

# funkciju argumentai (parametrai)
# def sudek_du_skaicius(skaicius1, skaicius2): #skaicius1 = 7 | skaicius2 = 9 # skaicius1 ir skaicius2 yra funkcijos parametrai

#     suma = skaicius1 + skaicius2
#     return suma


# print(sudek_du_skaicius(7,9)) # funkcijos iskvietimas
# sk1 = 7
# sk2 = 9
# print(sudek_du_skaicius(sk1,sk2))

# sk1 = 8+5+int(input("Ivesk pirma skaiciu: "))
# sk2 = int(input("Ivesk antra skaiciu: "))
# print(sudek_du_skaicius(sk1,sk2))


# def skaiciuok(skaicius1, skaicius2, veiksmas): # veiksmas = "+" | veiksmas = "-" | veiksmas = "*" | veiksmas = "/"
#     if veiksmas == "+":
#         return skaicius1 + skaicius2
#     elif veiksmas == "-":
#         return skaicius1 - skaicius2
#     elif veiksmas == "*":
#         return skaicius1 * skaicius2
#     elif veiksmas == "/":
#         if skaicius2 != 0:
#             return skaicius1 / skaicius2
#         else:
#             return "Dalyba is nulio negalima"
#     else:
#         return "Neteisingas veiksmas"
    
# print(skaiciuok(10,5,"+"))
# print(skaiciuok(10,5,"-"))
# print(skaiciuok(10,5,"*"))
# print(skaiciuok(10,5,"/"))

# suskaiciuojam
# sudek_du_skaicius(rezultatas, rezultatas2) 

# sarasas = [5,3,2,8,1,4]

# rezultatas = sum(sarasas) 

# print(rezultatas)

# def suma_daugyba(skaicius1=0, skaicius2=0, daugyba=1): # daugyba yra numatytasis parametras # jeigu funkcijos iskvietime nenurodysim trecio parametro, tada daugyba bus lygi 1
#     return (skaicius1 + skaicius2) * daugyba

# print(suma_daugyba())
# print(suma_daugyba(5))
# print(suma_daugyba(5,10))
# print(suma_daugyba(5,10,2))

# import datetime as dt

# dob = dt.datetime(1990,5,15) # date of birth
# print(dob)
# dob = dt.datetime(1990,5,15,14)
# print(dob)
# dob = dt.datetime(1990,5,15,14,30)
# print(dob)
# dob = dt.datetime(1990,5,15,14,30,45)
# print(dob)

# def suma_daugyba(skaicius1=0, skaicius2=0, daugyba): # daugyba yra numatytasis parametras # jeigu funkcijos iskvietime nenurodysim trecio parametro, tada daugyba bus lygi 1
#     return (skaicius1 + skaicius2) * daugyba

# print(suma_daugyba())
# print(suma_daugyba(5))
# print(suma_daugyba(5,10))
# print(suma_daugyba(7,5,2))
# def suma_daugyba(daugyba, skaicius1=0, skaicius2=0): # daugyba yra numatytasis parametras # jeigu funkcijos iskvietime nenurodysim trecio parametro, tada daugyba bus lygi 1
#     return (skaicius1 + skaicius2) * daugyba

# print(suma_daugyba())
# print(suma_daugyba(5))
# print(suma_daugyba(5,10))
# print(suma_daugyba(7))


# def suma_daugyba(skaicius1=0, skaicius2=0, daugyba=1): # daugyba yra numatytasis parametras # jeigu funkcijos iskvietime nenurodysim trecio parametro, tada daugyba bus lygi 1
#     return (skaicius1 + skaicius2) * daugyba

# print(suma_daugyba(skaicius2=7, daugyba=3)) # jeigu nurodome parametro pavadinima, tai galime keisti parametru eiliškuma

# def funkcija():
#     return 5

# print(funkcija())



