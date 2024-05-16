import os

def delete_key_file(key_file_path):
    """Apaga o arquivo de chave especificado se ele existir."""
    try:
        if os.path.exists(key_file_path):
            os.remove(key_file_path)
            print(f"Arquivo de chave '{key_file_path}' apagado com sucesso.")
        else:
            print(f"Arquivo de chave '{key_file_path}' não encontrado.")
    except Exception as e:
        print(f"Erro ao tentar apagar o arquivo de chave: {e}")


