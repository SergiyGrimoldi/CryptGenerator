import os 
from cryptography.fernet import Fernet
from os.path import join


encrypt_direcotry = "./example/"



def clear(): ## clear terminal/cmd display
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\nDecryption program by Sergiy Grimoldi\n\n")


try:
    clear()
    print("Searching for key...")

    files = []
    key_file = []

    for file in os.listdir("./"):
        key_file.append(file)

    if ("key.key") in key_file:
        print("Key found\nDecryption...\n")

        with open("key.key", "rb") as f:
            key = f.read()

        count_file = 0
        for dirname, dirnames, filenames in os.walk(encrypt_direcotry):
            for file in filenames:  # ciclo i files per averne il numero e nome
                if (file == ".DS_Store"):
                    continue # escludo file proprietari di sistema operativo MacOs
                count_file +=1

                file_tot = join(dirname,file) # genero file contentente anche la direcotry di appartenenenza
                
                files.append(file_tot) # aggiungo alla lista (lista)
        
        print(" - Decrypting: ",count_file, " files\n") # quanti file ho trovato nella directory (è un print di controllo visivo)

        for file in files:
            with open(file,"rb") as f:
                content = f.read()

                content_decrypted = Fernet(key).decrypt(content)

            with open(file,"wb") as f:
                f.write(content_decrypted)

            f.close()
        clear()
        print("Decrypted successfully.")
        print(" - Files decrypted: ",count_file, "\n")
        os.remove("./key.key")

    else:
        clear()
        print("Not key found")
except:
    clear()
    print("All file are decrypted.")
