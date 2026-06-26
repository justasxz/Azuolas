# with open("naujas.txt", "w") as file:
#     file.write("Sveikas pasauli!\n")
#     file.write("Tai yra naujas failas.\n")
#     file.write(str(15))

# with open("naujas.txt", "w") as file:
#     file.write(str([7,8,2,4]))



# with open("naujas.txt", "r") as file:
#     turinys = list(file.read())
#     print(turinys)

# turinys.append(10) # prideda 10 i saraso gala
# print(turinys)

import pickle

# sarasas = [7,8,2,4]
# with open("naujas.pickle", "wb") as file: # wb - write binary mode
#     pickle.dump(sarasas, file) # issaugo objekta i faila vietoje file.write naudojame pickle.dump(turinis, file)

with open("naujas.pickle", "rb") as file: # rb - read binary mode
    turinys = pickle.load(file) # nuskaito objekta is failo vietoje file.read naudojame pickle.load(file)
    print(turinys)

print(turinys)
turinys.append(10)
print(turinys)