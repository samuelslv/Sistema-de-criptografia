from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import os

def carregarChavePrivada(caminho, senha):
    # Carregar a chave privada de um arquivo com proteção por senha
    with open(caminho, 'rb') as key_file:
        chavePrivada = serialization.load_pem_private_key(
            key_file.read(),
            password=senha,
            backend=default_backend()
        )
    return chavePrivada

def carregarChavePublica(caminho):
    # Carregar a chave pública de um arquivo
    with open(caminho, 'rb') as key_file:
        chavePublica = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return chavePublica

def main(opcao):
    if opcao == 1:
        # Caminhos para os arquivos de chave
        private_key_caminho = 'chaves/private_key.pem'
        public_key_caminho = 'chaves/public_key.pem'

        # Senha usada para criptografar a chave privada
        senha = input("Coloque a senha para carregar a chave privada: ")
        # password = b'my_strong_password'

        # Carregar as chaves
        private_key = carregarChavePrivada(private_key_caminho, senha.encode("utf-8"))
        public_key = carregarChavePublica(public_key_caminho)
        print("Chave Privada Carregada:", private_key)
        print("Chave Pública Carregada:", public_key)
        return private_key, public_key

    elif opcao == 2:
        # Caminhos para os arquivos de chave
        public_key_caminho = 'chaves/public_key.pem'

        # Carregar as chaves
        public_key = carregarChavePublica(public_key_caminho)
        print("Chave Pública Carregada:", public_key)
        return public_key
