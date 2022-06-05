import os 
from cryptography.fernet import Fernet
from os.path import join


files = []
key_file = []
key_directory = "./"
encrypt_direcotry = "./example/"

def clear(): ## clear terminal/cmd display
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\nEncryption program by Sergiy Grimoldi\n\n")

def whattodo(): ## basic menu if key already exists
    choose = input("Encryption already done successfully.\nDo you want to decrypt?\n(Write <yes> to decrypt or <no> to exit.\n-> ")

    if choose.lower() == "yes":
        print("yes") ## insert command to run other file
        clear()
        os.system('python3 decrypt.py')
    elif choose.lower() == "no":
        print("No")
        clear()
        print("Exit.")
    else:
        clear()
        print("Invalid entry!\n")
        whattodo()

def searching_key(): ## search for key in directory choosen
    for file in os.listdir(key_directory):
        key_file.append(file)

def encryption(): ## creating key for encypt all files in directory to encrypt
    if not ("key.key") in key_file:
        print("Creating key...")
        count_file = 0
        for dirname, dirnames, filenames in os.walk(encrypt_direcotry):
            for file in filenames:  # ciclo i files per averne il numero e nome
                if (file == ".DS_Store"):
                    continue # escludo file proprietari di sistema operativo MacOs
                count_file +=1

                

                
                
                file_tot = join(dirname,file) # genero file contentente anche la direcotry di appartenenenza
                
                files.append(file_tot) # aggiungo alla lista (lista)
        
        print(" - Encrypting: ",count_file, " files\n") # quanti file ho trovato nella directory (è un print di controllo visivo)


        key = Fernet.generate_key()

        with open ("key.key", "wb") as f:
            f.write(key)

        f.close()


        for file in files:

            with open(file,"rb") as f:
                content = f.read()

                content_encrypted = Fernet(key).encrypt(content)

            with open(file,"wb") as f:
                f.write(content_encrypted)

            f.close()
        clear()
        print("Encrypted successfully.")
        print(" - Files encrypted: ",count_file, "\n")

    else:
        whattodo()





searching_key()
encryption()


