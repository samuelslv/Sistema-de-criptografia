from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

def Arquivo(diretorioEntrada, diretorioSaida, caminhoChave):
    with open(caminhoChave, 'rb') as key_file:
        chavePublica = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )



    # Certifique-se de que o diretório onde o arquivo criptografado será salvo existe
    os.makedirs(os.path.dirname(diretorioSaida), exist_ok=True)

    
    # Ler o conteúdo do arquivo
    with open(diretorioEntrada, 'rb') as f:
        plaintext = f.read()

    # Criptografar o conteúdo do arquivo
    ciphertext = chavePublica.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Escrever o conteúdo criptografado de volta para outro arquivo
    with open(diretorioSaida, 'wb') as f:
        f.write(ciphertext)

    print("Arquivo criptografado com sucesso e salvo em:", diretorioSaida)



