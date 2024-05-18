import shutil
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import os


def carregarChaves(nomeChave):
    origem = f"chaves_externas/{nomeChave}.pem"
    destino = f"chaves_importadas/{nomeChave}.pem"

    try:
        shutil.move(origem, destino)
        print(f"Arquivo movido de {origem} para {destino} com sucesso.")
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no caminho {origem}.")
    except IOError as e:
        print(f"Erro de E/S: {e}")
   