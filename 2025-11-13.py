# class Variklis():
#     def __init__(self, galia, tipas, turbo, cilindru_skaicius):
#         self.Galia = galia
#         self.Tipas = tipas
#         self.Turbo = turbo
#         self.Cilindru_skaicius = cilindru_skaicius



# class Car():
#     def __init__(self, color, price, make, model): # color = "Raudona"
#         self.Spalva = color
#         self.Kaina = price
#         self.Marke = make
#         self.Modelis = model
    
#     def __str__(self): # naudojamas viso objekto atvaizdavimui
#         return f"Automobilis: {self.Marke} {self.Modelis}, Spalva: {self.Spalva}, Kaina: {self.Kaina} EUR"
#     def __repr__(self): # naudojamas kai objektas sarase ar kituose konteineriuose atvaizduojamas (skiriasi nuo __str__ del to nes ne visados norime atvaizduoti pilna objekta, kai jis yra sarase)
#         return f"Automobilis: {self.Marke} {self.Modelis}, Spalva: {self.Spalva}, Kaina: {self.Kaina} EUR"
    
#     def uzsikurti(self, kuras): # self = mano_automobilis1
#         print(f"Automobilis {self.Marke} uzsikure naudodamas {kuras}")


# variklis1 = Variklis(150, "Benzinas", True, 4)
# variklis2 = Variklis(200, "Dyzelis", False, 6)


# mano_automobilis = Car("Raudona",50000, "Toyota", "Corolla") # objekto inicializavimas (sukurimas)
# mano_automobilis1 = Car("Melyna",15000, "Audi", "A6") # objekto inicializavimas (sukurimas)
# mano_automobilis2 = Car("Juoda",30000, "VW", "Golf") # objekto inicializavimas (sukurimas)

# mano_automobilis.uzsikurti("Dyzeliu")
# mano_automobilis1.uzsikurti("Benzinu")

# print(mano_automobilis1.Spalva)# laisvai galima prieiti prie objekto savybiu
# mano_automobilis.Kaina = 45000 # keiciame objekto savybes 

# print(mano_automobilis.Kaina)
# print(mano_automobilis1.Spalva)
# print(mano_automobilis2.Kaina)

# skaicius = 15
# skaicius2 = 20

# skaiciai = [skaicius, skaicius2]
# automobiliai = [mano_automobilis, mano_automobilis1]
# automobiliai.append(mano_automobilis2)

# for auto in automobiliai:
#     print(f"Automobilio spalva: {auto.Spalva}, kaina: {auto.Kaina}")

# print(mano_automobilis)
# print(mano_automobilis1)
# print(mano_automobilis2)

# print("Pabaiga")





# def daryk_ka(color):
#     pass

# daryk_ka("Melyna")



import pickle

class Variklis():
    def __init__(self, galia, tipas, turbo, cilindru_skaicius):
        self.Galia = galia
        self.Tipas = tipas
        self.Turbo = turbo
        self.Cilindru_skaicius = cilindru_skaicius



class Car():
    def __init__(self, color, price, make, model, engine): # color = "Raudona"
        self.Spalva = color
        self.Kaina = price
        self.Marke = make
        self.Modelis = model
        self.Variklis = engine
    
    def __str__(self): # naudojamas viso objekto atvaizdavimui
        return f"Automobilis: {self.Marke} {self.Modelis}, Spalva: {self.Spalva}, Kaina: {self.Kaina} EUR ir Variklis: {self.Variklis.Galia} AG, {self.Variklis.Tipas}"
    def __repr__(self): # naudojamas kai objektas sarase ar kituose konteineriuose atvaizduojamas (skiriasi nuo __str__ del to nes ne visados norime atvaizduoti pilna objekta, kai jis yra sarase)
        return f"Automobilis: {self.Marke} {self.Modelis}, Spalva: {self.Spalva}, Kaina: {self.Kaina} EUR"
    
    def uzsikurti(self, kuras): # self = mano_automobilis1
        print(f"Automobilis {self.Marke} uzsikure naudodamas {kuras}")


# variklis1 = Variklis(150, "Benzinas", True, 4)
# variklis2 = Variklis(200, "Dyzelis", False, 6)


# mano_automobilis = Car("Raudona",50000, "Toyota", "Corolla", variklis1) # objekto inicializavimas (sukurimas)

# print(mano_automobilis)
# print(mano_automobilis.Variklis.Galia)



# with open("automobilis.pkl", "wb") as f:
#     pickle.dump(mano_automobilis, f)

with open("automobilis.pkl", "rb") as f:
    naujas_automobilis = pickle.load(f)
print(naujas_automobilis)
naujas_automobilis.uzsikurti("Benzinu")
print(naujas_automobilis.Variklis.Tipas)

# I faila irasom Car ("Raudona",50000, "Toyota", "Corolla", variklis1)