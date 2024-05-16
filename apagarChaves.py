import os

def deletarChave(chaveCaminho):
    try:
        if os.path.exists(chaveCaminho):
            os.remove(chaveCaminho)
            print(f"Arquivo de chave '{chaveCaminho}' apagado com sucesso.")
        else:
            print(f"Arquivo de chave '{chaveCaminho}' não encontrado.")
    except Exception as e:
        print(f"Erro ao tentar apagar o arquivo de chave: {e}")


