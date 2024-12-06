from cryptography.fernet import Fernet


def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    
    print(f"Arquivo '{filename}' foi descriptografado com sucesso.")


if __name__ == "__main__":
    filename = input("Digite o nome do arquivo a ser descriptografado (inclua a extensão): ")
    decrypt_file(filename)