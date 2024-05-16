import os

def listar(directory, file_extension=".pem"):
    """Lista todos os arquivos de chave no diretório especificado com a extensão dada."""
    # Lista para armazenar os caminhos completos dos arquivos de chave
    chaves = []

    # Percorrer os arquivos no diretório
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            # Construir o caminho completo do arquivo
            file_path = os.path.join(directory, filename)
            chaves.append(file_path)

    return chaves


