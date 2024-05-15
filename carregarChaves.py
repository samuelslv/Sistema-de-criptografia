from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import os


class carregar:

    def load_private_key(path, password):
        # Carregar a chave privada de um arquivo com proteção por senha
        with open(path, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=password,
                backend=default_backend()
            )
        return private_key

    def load_public_key(path):
        # Carregar a chave pública de um arquivo
        with open(path, 'rb') as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key

    def main(opcao):
        if opcao == 1:
            # Caminhos para os arquivos de chave
            private_key_path = 'private_key.pem'
            public_key_path = 'public_key.pem'

            # Senha usada para criptografar a chave privada
            password = b'my_strong_password'

            # Carregar as chaves
            private_key = carregar.load_private_key(private_key_path, password)
            public_key = carregar.load_public_key(public_key_path)
            print("Chave Privada Carregada:", private_key)
            print("Chave Pública Carregada:", public_key)

        elif opcao == 2:
            # Caminhos para os arquivos de chave
            public_key_path = 'public_key.pem'

            # Carregar as chaves
            public_key = carregar.load_public_key(public_key_path)
            print("Chave Pública Carregada:", public_key)
 

