from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Chave gerada e salva no arquivo 'key.key'.")


def encrypt_file(filename):
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    
    fernet = Fernet(key)
    
    with open(filename, "rb") as file:
        original_data = file.read()
    
    encrypted_data = fernet.encrypt(original_data)
    
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    
    print(f"Arquivo '{filename}' foi criptografado com sucesso.")


if __name__ == "__main__":
    filename = input("Digite o nome do arquivo a ser criptografado (inclua a extensão): ")
    generate_key()
    encrypt_file(filename)