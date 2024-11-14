import argparse
import os
from cryptography.fernet import Fernet

## Genererar och sparar en krypteringsnyckel ##
def generate_key():  ## Definierar en funktion med namnet 'generate_key ##
    key = Fernet.generate_key()  ## Skapar en nyckel med fernet och lagrar den i variablen 'key' ##
    with open("encryption.key", "wb") as key_file:  ## Öppnar en fil med namnet 'encryption.key' i binärt skrivläge ##
        key_file.write(key)  ## Skriver den genererade nyckel till filen 'key_file' ##
    print("Nyckel genererad och sparad som 'encryption.key'.")  ## Skriver ut det i printen när du genererat en nyckel ##

## Ladda nyckeln från filen 'encryption.key' ##
def load_key():  ## Definierar en funktion med namnet 'Load_key
    with open("encryption.key", "rb") as key_file:  ## Öppnar 'encryption.key' i binärt läsläge och läser in nyckeln ##
        return key_file.read()  ## Läser in och retunerar nyckeln från filen ##

## Krypterar och gör om filen till en krypterad fil ##
def encrypt_file(file_path, key):  ## Definierar en funktion med namnet 'encrypt_file'. Tar emot filsökväg och krypteringsnyckeln ##
    with open(file_path, "rb") as file: ## Öppnar filen som ska krypteras i binärt läsläge ##
        encrypted_data = Fernet(key).encrypt(file.read())  ## Läser filens innehåll och krypterar den med nyckeln. Lagras i variabeln 'encrypted_data'
    with open(file_path + ".encrypted", "wb") as file:  ## Skapar filen men lägger till '.encrypted'. Är i binärt skrivläge ##
        file.write(encrypted_data)  ## Skriver den krypterade datan till den nya filen ##
    os.remove(file_path)  ## Tar bort den ursprungliga okrypterade filen ##
    print(f"'{file_path}' har krypterats, den krypterade filen heter nu '{file_path}.encrypted'.")  ## Printar ut meddelandet när man har krypterat filen ##

## Dekryptera den krypterade filen och gör om den till en vanlig fil ##
def decrypt_file(file_path, key):  ## Definierar en funktion med namnet 'decrypt_file'. Tar emot filsökväg och krypteringsnyckeln ##
    with open(file_path, "rb") as file:  ## Öppnar den krypterade filen i binärt läsläge ##
        decrypted_data = Fernet(key).decrypt(file.read())  ## Läser in och dekrypterar filens innehåll. Lagrar den dekrypterade datan i variabeln 'decrypted_dara' ##
    with open(file_path.replace(".encrypted", ""), "wb") as file:  ## Skapar en ny fil med ursprungsnamnet och tar bort '.encrypted'. Är i binärt skrivläge ##
        file.write(decrypted_data)  ## Skriver den dekrypterade datan till den nya filen ##
    os.remove(file_path) ## Tar bort den krypterade filen ##
    print(f"'{file_path}' har dekrypterats och heter nu '{file_path.replace('.encrypted', '')}'.")  ## Skriver ut ett meddelande när filen har dekrypterats ##

def main():  ## Definierar huvudfunktionen som tar in argument i terminalen
    
    parser = argparse.ArgumentParser(description="Verktyg för att kryptera och dekryptera filer.")  ## Ger en kort beskrivning av vad programmet gör ##
    parser.add_argument("command", choices=["generate-key", "encrypt", "decrypt"], help="Välj något av de tre kommandona att använda följt av filnamnet.") ## Här är det obligatoriska kommandon som måste användas för att kunna hantera det här programmet ##
    parser.add_argument("file", nargs="?", help="Filen att kryptera eller dekryptera.") ## Det definierar file-argumentet som används för att specificera vilken fil som ska krypteras eller dekrypteras ##
    args = parser.parse_args()  ## Tolkar argumenten som skrivs in och lägger de i variabel 'args' ##

    ## En if sats som anropar funktioner för att generera en nyckel, kryptera eller dekryptera ##
    if args.command == "generate-key":
        generate_key()
    elif args.command == "encrypt" and args.file:
        encrypt_file(args.file, load_key())
    elif args.command == "decrypt" and args.file:
        decrypt_file(args.file, load_key())
    else:
        parser.print_help()  ## Om inget giltigt argument körs så får man hjälp i terminalen vad man ska skriva ##
        
if __name__ == "__main__":
    main()