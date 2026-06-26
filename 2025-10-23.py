import os # operating system

# os most important functions
print("Current Working Directory:", os.getcwd())  # Get current working directory
# new_dir = r"C:\Users\guiku\Desktop\NewFolder12345" # absolute path
# new_dir = "NewFolder12345/anothernew" # relative/local
# new_dir = "NewDir" # relative/local
# os.mkdir(new_dir)  # Create a new directory


# os.chdir(new_dir)  # Change to the new directory
# print("Changed Working Directory:", os.getcwd())
# local vs global path
# local path is relative to the current working directory
# other important functions
# os.rename("file_to_rename.txt", "renamed_file.txt")  # Rename a file
# os.remove("renamed_file.txt")  # Remove a file
# os.rmdir("NewDir")  # Remove a directory (only if empty)
# os.chdir("..")  # Go back to the parent directory
# print("Back to Parent Directory:", os.getcwd())
# print("Listing files and directories in current directory:")
# print(os.listdir())  # List files and directories in the current directory
# failu_sarasas = os.listdir()
# for failas in failu_sarasas:
#     print(" -", failas)
# os.path module
# file_path = os.path.join(os.getcwd(), "bak.py")  # Join paths 
# # print("Joined File Path:", file_path)
# # print("Does the file exist?", os.path.exists(file_path))  # Check if a path
# # print("Is it a file?", os.path.isfile(file_path))  # Check if it's a file
# # print("Is it a directory?", os.path.isdir(file_path))  # Check if it's a
# print("File size in bytes:", os.path.getsize(file_path))  # Get file size
# print("File last modified time:", os.path.getmtime(file_path))  # Get last modified time

# import datetime as dt
# mod_time = os.path.getmtime(file_path)
# mod_time_readable = dt.datetime.fromtimestamp(mod_time)
# print("Last modified time (readable):", mod_time_readable)

# let's open a file and write something to it
# failas = open("naujas.txt", "w")  # open file in write mode w - write rezimas (jeigu failas neegzistuoja, jis bus sukurtas)
# failas.write("Sveikas pasauli!\n")
# failas.write("Tai yra naujas failas.\n")
# failas.close()

# print("Labas\nKaip\nsekasi")
# with open("naujas.txt", "w") as file: # file = open("naujas.txt", "w") (write istrina sena turini ir raso nauja)
#     file.write("Sveikas pasauli!\n")
#     file.write("Tai yra naujas failas.\n")

# with open("naujas.txt", "r") as file: # r - read mode (read has to have a file to read)
#     turinys = file.read()
#     # turinys = file.readlines() # grazina sarasa, kur kiekviena eilute yra atskiras elementas
#     # while True:
#     #     eilute = file.readline()
#     #     if not eilute: # ar eilutes nesibaigia (not apsuka)
#     #         break
#     #     print(eilute.strip()) # strip() - pasalina tarpus ir naujos eilutes simbolius is priekio ir galo
#     print(turinys)

# file.close() # automaticly closed when using 'with' statement

# with open("naujas.txt", "a") as file: # a - append mode (prideda nauja turini prie esamo, jei failas neegzistuoja, jis bus sukurtas)
#     file.write("Sveikas pasauli!\n")
#     file.write("Tai yra naujas failas.\n")