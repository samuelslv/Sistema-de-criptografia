from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def gerar_chaves():
    # Gerar a chave privada
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    # Derivar a chave pública da chave privada
    public_key = private_key.public_key()

    # Serializar a chave privada com proteção de senha (PEM format)
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(
            b'my_strong_password')
    )

    # Serializar a chave pública (PEM format)
    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Salvar as chaves em arquivos
    #with open('private_key.pem', 'wb') as f:
    #    f.write(pem_private_key)
    #with open('public_key.pem', 'wb') as f:
    #    f.write(pem_public_key)

    print("Chaves geradas e salvas com sucesso!")

    return pem_public_key, pem_private_key


# gerar_chave()
