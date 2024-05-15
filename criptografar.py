from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

def Arquivo(input_file_path, output_file_path, public_key):
    # Certifique-se de que o diretório onde o arquivo criptografado será salvo existe
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    
    # Ler o conteúdo do arquivo
    with open(input_file_path, 'rb') as f:
        plaintext = f.read()

    # Criptografar o conteúdo do arquivo
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Escrever o conteúdo criptografado de volta para outro arquivo
    with open(output_file_path, 'wb') as f:
        f.write(ciphertext)

    print("Arquivo criptografado com sucesso e salvo em:", output_file_path)

# Suponha que 'public_key' seja a chave pública RSA carregada
# encrypt_file('path/to/your/file.txt', 'path/to/your/encrypted_file.enc', public_key)
