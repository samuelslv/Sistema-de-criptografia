import os

def salvarAmbas(caminho, pem_public_key, pem_private_key, nomeEscolhidoChaves):
    # Certifique-se de que o diretório onde o arquivo criptografado será salvo existe
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    caminho1 = f"chaves/{nomeEscolhidoChaves}_public.pem"
    caminho2 = f"chaves/{nomeEscolhidoChaves}_private.pem"
    # Salvar as chaves em arquivos
    with open(caminho2, 'wb') as f:
        f.write(pem_private_key)
    with open(caminho1, 'wb') as f:
        f.write(pem_public_key)
    
    print("Sucesso na exportação de ambas as chaves")

def salvarPublica(caminho, pem_public_key, nomeEscolhidoChaves):
    # Certifique-se de que o diretório onde o arquivo criptografado será salvo existe
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
        # Salvar as chaves em arquivos
    caminho = f"chaves/{nomeEscolhidoChaves}.pem"
    with open(caminho, 'wb') as f:
        f.write(pem_public_key)

    print("Sucesso na exportação da chave pública")


