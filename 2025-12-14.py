# darbuotojas ir klientas
# darbuotojas turi vardą, pavardę ir atlyginimą
# klientas turi vardą, pavardę ir sąskaitos likutį
# class Human:
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde

#     def __str__(self):
#         return f"As esu {self.vardas} {self.pavarde}"
#     def gyventi(self):
#         print(f"{self.vardas} gyvena savo gyvenimą.")
#     def dirbti(self):
#         print(f"{self.vardas} dirba savo darba")

# class Darbuotojas(Human): # paveldi iš Human
#     def __init__(self, vardas, pavarde, atlyginimas): # parametrai pareina visi, nes turim nurodyti, reiksmes
#         super().__init__(vardas, pavarde)  # kvieciame tevine klases konstruktoriu
#         self.atlyginimas = atlyginimas # papildomas parametras tik Darbuotojas klasei

#     def __str__(self):
#         return f"Darbuotojas: {self.vardas} {self.pavarde}, Atlyginimas: {self.atlyginimas} EUR"
    
#     def dirbti(self):
#         print(f"{self.vardas} dirba savo darba sioje imoneje")

#     def parduoti(self):
#         print("As parduodu")
# class Klientas(Human): # paveldi iš Human
#     def __init__(self, vardas, pavarde, saskaitos_likutis):
#         super().__init__(vardas, pavarde)
#         self.saskaitos_likutis = saskaitos_likutis
#     def dirbti(self):
#         print(f"{self.vardas} dirba savo kazkur kitur")

#     def pirkti(self):
#         print("as perku")
#     # def __str__(self):
#     #     return f"Klientas: {self.vardas} {self.pavarde}, Sąskaitos likutis: {self.saskaitos_likutis} EUR"

# darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 1500)
# darbuotojas2 = Darbuotojas("Antanas", "Antanaitis", 1500)
# darbuotojas3 = Darbuotojas("Marius", "maraitis", 1500)
# klientas1 = Klientas("Kestas", "Kestaitis", 3000)
# klientas2 = Klientas("Paulius", "Paulaitis", 3000)
# klientas3 = Klientas("Denis", "Denaitis", 3000)

# zmogus = Human("Justas","Justaitis")


# class Universitetas():
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.studentai = []
#     def __str__(self):
#         return f"Universitetas: {self.pavadinimas}"

# class Studentas():
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pazymiai = []
#     def __str__(self):
#         return f"Studentas {self.vardas} {self.pavarde}, kurio pazymiai {self.pazymiai}"
#     def __repr__(self):
#         return f"{self.vardas} {self.pavarde}"
#     def vidurkis(self):
#         return sum(self.pazymiai)/len(self.pazymiai)    

# stud1 = Studentas("Jonas","Jonaitis")
# stud2 = Studentas("Karolis","Karolaitis")
# stud3 = Studentas("Marius","Maraitis")

# stud1.pazymiai.append(8)
# stud1.pazymiai.append(7)
# stud1.pazymiai.append(9)
# stud1.pazymiai.append(10)


# stud2.pazymiai.append(2)
# stud2.pazymiai.append(5)
# stud2.pazymiai.append(9)
# stud2.pazymiai.append(10)

# stud3.pazymiai.append(4)
# stud3.pazymiai.append(7)
# stud3.pazymiai.append(9)
# stud3.pazymiai.append(3)

# print(stud1)
# print(stud1.vidurkis())

# univeras = Universitetas("KTU")
# univeras.studentai.append(stud1)
# univeras.studentai.append(stud2)
# univeras.studentai.append(stud3)
# print(univeras)
# print(univeras.studentai)

# for stud in univeras.studentai:
