import argparse
import os
from cryptography.fernet import Fernet

## Genererar och sparar en krypteringsnyckel ##
def generate_key():
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)
    print("Nyckel genererad och sparad som 'encryption.key'.")

## Ladda nyckeln från filen 'encryption.key' ##
def load_key():
    with open("encryption.key", "rb") as key_file:
        return key_file.read()

## Krypterar och gör om filen till en krypterad fil ##
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = Fernet(key).encrypt(file.read())
    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    os.remove(file_path)
    print(f"'{file_path}' har krypterats, den krypterade filen heter nu '{file_path}.encrypted'.")

## Dekryptera den krypterade filen och gör om den till en vanlig fil ##
def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        decrypted_data = Fernet(key).decrypt(file.read())
    with open(file_path.replace(".encrypted", ""), "wb") as file:
        file.write(decrypted_data)
    os.remove(file_path)
    print(f"'{file_path}' har dekrypterats och heter nu '{file_path.replace('.encrypted', '')}'.")

def main():
    
    parser = argparse.ArgumentParser(description="Verktyg för att kryptera och dekryptera filer.")
    parser.add_argument("command", choices=["generate-key", "encrypt", "decrypt"], help="Välj något av de tre arguments att använda följt av filnamnet.")
    parser.add_argument("file", nargs="?", help="Filen att kryptera eller dekryptera.")
    args = parser.parse_args()

    if args.command == "generate-key":
        generate_key()
    elif args.command == "encrypt" and args.file:
        encrypt_file(args.file, load_key())
    elif args.command == "decrypt" and args.file:
        decrypt_file(args.file, load_key())
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()