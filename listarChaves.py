import os

def listar(diretorio, file_extension=".pem"):
    """Lista todos os arquivos de chave no diretório especificado com a extensão dada."""
    # Lista para armazenar os caminhos completos dos arquivos de chave
    chaves = []

    # Percorrer os arquivos no diretório
    for filename in os.listdir(diretorio):
        if filename.endswith(file_extension):
            # Construir o caminho completo do arquivo
            file_path = os.path.join(diretorio, filename)
            chaves.append(file_path)

    return chaves


def listarArquivos(diretorio, file_extension=".enc"):
    """Lista todos os arquivos de texto no diretório especificado com a extensão dada."""
    # Lista para armazenar os caminhos completos dos arquivos de texto
    arquivos = []

    # Percorrer os arquivos no diretório
    for filename in os.listdir(diretorio):
        if filename.endswith(file_extension):
            # Construir o caminho completo do arquivo
            file_path = os.path.join(diretorio, filename)
            arquivos.append(file_path)

    return arquivos