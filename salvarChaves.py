        
def salvarAmbas(pem_public_key, pem_private_key):
    # Salvar as chaves em arquivos
    with open('private_key.pem', 'wb') as f:
        f.write(pem_private_key)
    with open('public_key.pem', 'wb') as f:
        f.write(pem_public_key)
    
    print("Sucesso na importação de ambas as chaves")

def salvarPublica(pem_public_key):
        # Salvar as chaves em arquivos
    with open('public_key.pem', 'wb') as f:
        f.write(pem_public_key)

    print("Sucesso na importação da chave publica")


