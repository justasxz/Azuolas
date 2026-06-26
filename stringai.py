tekstas = "Labas Mano pasauli! Man patinka programuoti."

# print(tekstas[::-2]) # [start:stop:step]

# print(tekstas.upper())
# print(tekstas.lower())
# print(tekstas.capitalize())
# print(tekstas.title())
# print(tekstas.count("Man"))
# print(tekstas.find("Man")) # grazina pirmo radimo indeksa

# ar tekste egzistuoja zodis patinka
# if tekstas.find("patinka") != -1: # jeigu find rezultatas nera -1
#     print("Zodis egzistuoja")
# else:
#     print("Zodis neegzistuoja")

# if tekstas.find("patinka") == -1: # jeigu find rezultatas nera -1
#     print("Zodis neegzistuoja")
# else:
#     print("Zodis egzistuoja")

# print(tekstas.replace("a", "XX")) 
# vardas = input("Ivesk savo varda:")
# if vardas.lower() == "justas":
#     print("Zodziai lygus")
 # pasalina tarpus is priekio ir galo
# print(tekstas.strip())
# print(tekstas.split(" ")) # is teksto padaro sarasa pagal nurodyta skyrikli
# skaiciai = "15a"

# if skaiciai.isdigit(): # patikrina ar stringas yra sudarytas is skaiciu
#     print("Stringas yra skaicius")
#     skaicius = int(skaiciai) # konvertuoja stringa i int
#     print(skaicius + 5)

# ivestis = (input("Iveskite skaicius: "))
# sarasas = ivestis.split(",")

# nauji_skaiciai = []

# for skaicius in sarasas:
#     nauji_skaiciai.append(int(skaicius))
 
# print(sum(nauji_skaiciai))

# dict1 = {
#     "vardas": "Justas",
#     "amzius": 25,
#     "miestas": "Vilnius"
# }

# if dict1.get("vardass") == None: # patikrina ar egzistuoja raktas vardas
#     print("Raktas neegzistuoja")