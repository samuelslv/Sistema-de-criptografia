from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import os

def Arquivo(encrypted_file_path, output_file_path, private_key):
    # Certifique-se de que o diretório onde o arquivo criptografado será salvo existe
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)    
    
    # Ler o conteúdo criptografado do arquivo
    with open(encrypted_file_path, 'rb') as file:
        ciphertext = file.read()

    # Descriptografar o conteúdo do arquivo
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Salvar o conteúdo descriptografado em um novo arquivo
    with open(output_file_path, 'wb') as file:
        file.write(plaintext)

    print("Arquivo descriptografado com sucesso e salvo em:", output_file_path)

# Exemplo de carregar a chave privada (supondo que você tenha a senha)
def load_private_key(path, password):
    with open(path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=password,
            backend=default_backend()
        )
    return private_key


