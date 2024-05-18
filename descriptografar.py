from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import os

def Arquivo(arquivoEncriptado, ArquivoSaida, caminhoChavePrivada, senha):

    senha = senha.encode("utf-8")
    # Carregar a chave privada de um arquivo com proteção por senha
    with open(caminhoChavePrivada, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=senha,
            backend=default_backend()
        )

    # Certifique-se de que o diretório onde o arquivo criptografado será salvo existe
    os.makedirs(os.path.dirname(ArquivoSaida), exist_ok=True)    
    
    # Ler o conteúdo criptografado do arquivo
    with open(arquivoEncriptado, 'rb') as file:
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
    with open(ArquivoSaida, 'wb') as file:
        file.write(plaintext)

    print("Arquivo descriptografado com sucesso e salvo em:", ArquivoSaida)

# Exemplo de carregar a chave privada (supondo que você tenha a senha)
def carregarChavePrivada(caminho, senha):
    with open(caminho, 'rb') as key_file:
        chavePrivada = serialization.load_pem_private_key(
            key_file.read(),
            password=senha,
            backend=default_backend()
        )
    return chavePrivada


