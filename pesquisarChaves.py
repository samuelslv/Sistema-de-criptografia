import os

def buscarChave(directory, search_term, file_extension=".pem"):
    """Pesquisa arquivos de chave que contêm o termo de pesquisa no nome do arquivo, dentro do diretório especificado."""
    # Lista para armazenar os caminhos completos dos arquivos de chave que correspondem ao termo de pesquisa
    chavesEncontradas = []

    # Percorrer os arquivos no diretório
    for filename in os.listdir(directory):
        if filename.endswith(file_extension) and search_term in filename:
            # Construir o caminho completo do arquivo
            file_path = os.path.join(directory, filename)
            chavesEncontradas.append(file_path)

    return chavesEncontradas


