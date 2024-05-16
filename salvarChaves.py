import os

def salvarAmbas(caminho, pem_public_key, pem_private_key):
    # Certifique-se de que o diretório onde o arquivo criptografado será salvo existe
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    # Salvar as chaves em arquivos
    with open('chaves/private_key.pem', 'wb') as f:
        f.write(pem_private_key)
    with open('chaves/public_key.pem', 'wb') as f:
        f.write(pem_public_key)
    
    print("Sucesso na exportação de ambas as chaves")

def salvarPublica(caminho, pem_public_key):
    # Certifique-se de que o diretório onde o arquivo criptografado será salvo existe
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
        # Salvar as chaves em arquivos
    with open('chaves/public_key.pem', 'wb') as f:
        f.write(pem_public_key)

    print("Sucesso na exportação da chave pública")


