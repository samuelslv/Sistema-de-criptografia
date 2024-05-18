from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import gerarChaves
import salvarChaves
import carregarChaves
import criptografar
import descriptografar
import listarChaves
import pesquisarChaves
import apagarChaves
from getpass import getpass

# Variáveis globais para armazenar as chaves durante a execução do script
chavePrivada = None
chavePublica = None
nomeEscolhidoChaves = ""


def main():
    global chavePrivada, chavePublica
    while True:
        print("\n=== Sistema de Gerenciamento de Chaves Públicas e Criptografia ===")
        print("1. Gerar Par de Chaves")
        print("2. Exportar Chaves")
        print("3. Importar Chaves")
        print("4. Criptografar arquivos")
        print("5. Descriptografar arquivos")
        print("6. Listar Chaves")
        print("7. Pesquisar Chaves")
        print("8. Apagar Chaves")
        print("9. Sair")
        escolha = input("Escolha uma opção: ")

        match int(escolha):
            case 1:
                
                while True:
                    nome = input("Digite o nome para as chaves: ")
                    diretorio = "chaves/"
                    nome1 = nome + "_private.pem"
                    nome2 = nome + "_public.pem"
                    chaveEncontrada1 = pesquisarChaves.buscarChave(diretorio, nome1)
                    chaveEncontrada2 = pesquisarChaves.buscarChave(diretorio, nome2)
                    if len(chaveEncontrada1) != 0 or len(chaveEncontrada2) != 0:
                        print("Chave já existe")                    
                    else:
                        nomeEscolhidoChaves = nome
                        break

                chavePublica, chavePrivada = gerarChaves.gerar_chaves()

            case 2:
                if chavePublica == None:
                    print(
                        "Antes de exportar é necessário gerar as chaves. Retornando para o menu principal")
                else:
                    caminho = 'chaves/'
                    print("Escolha qual chave exportar:")
                    print('1-As duas chaves\n2-Somente a chave pública')
                    escolha = input("Escolher: ")
                    if escolha == '1':
                        salvarChaves.salvarAmbas(caminho, chavePublica, chavePrivada, nomeEscolhidoChaves)
                    elif escolha == '2':
                        salvarChaves.salvarPublica(caminho, chavePublica, nomeEscolhidoChaves)
                    else:
                        print("opção incorreta! Retornando para o menu principal")

            case 3:
                # print("Escolha qual chave importar:")
                # print('1-As duas chaves\n2-Somente a chave pública')
                # escolha = input("Escolher: ")
                # if escolha == '1':
                #     chavePrivada, chavePublica = carregarChaves.main(1)
                # elif escolha == '2':
                #     chavePublica = carregarChaves.main(2)
                # else:
                #     print("opcao incorreta! Retornando para o menu principal")
                diretorio = "chaves_externas/"
                chaves = listarChaves.listar('chaves_externas/', ".pem")
                if len(chaves) == 0:
                    print("Nenhuma chave encontrada no diretório especificado.")
                else:
                    print("Chaves encontradas:")
                    for chave in chaves:
                        print(chave)
                    nomeChave = input("Digite o nome da chave publica a ser importada: ")
                    chaveEncontrada = pesquisarChaves.buscarChave(diretorio, nomeChave)
                    if len(chaveEncontrada) == 0:
                        print("Chave não encontrada")
                        
                    else:
                        for chave in chaveEncontrada:
                            print("Chave encontrada:", chave)
                            carregarChaves.carregarChaves(nomeChave)
            case 4:
                opcao = input("Deseja utilizar chave pessoal ou importada? 1 - Pessoal, 2 - Importada: ")
                if opcao == '1':
                    diretorio = "chaves/"
                    chaves = listarChaves.listar('chaves/', ".pem")
                    if len(chaves) == 0:
                        print("Nenhuma chave encontrada no diretório especificado.")
                    else:
                        print("Chaves encontradas:")
                        for chave in chaves:
                            print(chave)
                        termoBuscado = input("Digite o nome da chave publica a ser usada para a criptografia: ")
                        chaveEncontrada = pesquisarChaves.buscarChave(diretorio, termoBuscado)
                        if len(chaveEncontrada) == 0:
                            print("Chave não encontrada")
                        else:
                            for chave in chaveEncontrada:
                                print("Chave encontrada:", chave)

                        diretorioSaida = f"criptografados/{termoBuscado}_encrypted_file.enc"

                        criptografar.Arquivo('texto.txt', diretorioSaida, chave) 
                elif opcao == '2':
                    diretorio = "chaves_importadas/"
                    chaves = listarChaves.listar('chaves_importadas/', ".pem")
                    if len(chaves) == 0:
                        print("Nenhuma chave encontrada no diretório especificado.")
                    else:
                        print("Chaves encontradas:")
                        for chave in chaves:
                            print(chave)
                        termoBuscado = input("Digite o nome da chave publica a ser usada para a criptografia: ")
                        chaveEncontrada = pesquisarChaves.buscarChave(diretorio, termoBuscado)
                        if len(chaveEncontrada) == 0:
                            print("Chave não encontrada")
                        else:
                            for chave in chaveEncontrada:
                                print("Chave encontrada:", chave)
                            senha = input("Insira a senha da chave privada: ")
                            diretorioSaida = f"criptografados/{termoBuscado}_encrypted_file.enc"
                            criptografar.Arquivo('texto.txt', diretorioSaida, chave, senha) 
                           
                    
            case 5:
                diretorio = "criptografados/"
                arquivos = listarChaves.listarArquivos('criptografados/', ".enc")
                if len(arquivos) == 0:
                    print("Nenhum arquivo criptografado encontrado no diretório especificado.")
                else:
                    print("Arquivos criptografados encontrados:")
                    for arquivo in arquivos:
                        print(arquivo)
                termoBuscado1 = input("Digite o nome do arquivo criptografado a ser descriptografado: ")
                arquivoEncontrado = pesquisarChaves.buscarArquivo(diretorio, termoBuscado1)
                if len(arquivoEncontrado) == 0:
                    print("Arquivo não encontrado")
                else:
                    for arquivo in arquivoEncontrado:
                        print("Arquivo encontrado:", arquivo)
                
                diretorio = "chaves/"
                chaves = listarChaves.listar('chaves/', ".pem")
                if len(chaves) == 0:
                    print("Nenhuma chave encontrada no diretório especificado.")
                else:
                    print("Chaves encontradas:")
                    for chave in chaves:
                        print(chave)
                    termoBuscado = input("Digite o nome da chave privada a ser usada para a descriptografia: ")
                    chaveEncontrada = pesquisarChaves.buscarChave(diretorio, termoBuscado)
                    if len(chaveEncontrada) == 0:
                        print("Chave não encontrada")
                    else:
                        for chave in chaveEncontrada:
                            print("Chave encontrada:", chave)
                




                senha = input("Insira a senha da chave privada: ")
                destino = f"descriptografados/{termoBuscado}_decrypted_file.txt"
                descriptografar.Arquivo(arquivo, destino, chave, senha)
            case 6:                
                chaves = listarChaves.listar('chaves/', ".pem")
                if len(chaves) == 0:
                    print("Nenhuma chave encontrada no diretório especificado.")
                else:
                    print("Chaves encontradas:")
                    for chave in chaves:
                        print(chave)
            case 7:
                diretorio = "chaves/"
                chaves = listarChaves.listar('chaves/', ".pem")
                if len(chaves) == 0:
                    print("Nenhuma chave encontrada no diretório especificado.")
                else:
                    print("Chaves encontradas:")
                    for chave in chaves:
                        print(chave)
                    termoBuscado = input("Digite o nome da chave para pesquisar: ")
                    chaveEncontrada = pesquisarChaves.buscarChave(diretorio, termoBuscado)
                    if len(chaveEncontrada) == 0:
                        print("Chave não encontrada")
                    else:
                        for chave in chaveEncontrada:
                            print("Chave encontrada:", chave)
            case 8:
                chaves = listarChaves.listar('chaves/', ".pem")
                if len(chaves) == 0:
                    print("Nenhuma chave encontrada no diretório especificado.")
                else:
                    print("Chaves encontradas:")
                    for chave in chaves:
                        print(chave)
                    nomeChave = input("Digite somente o nome da chave que deseja apagar: ")  # Substitua pelo caminho completo do arquivo de chave
                    diretorio = "chaves/"+ nomeChave +".pem"
                    
                    apagarChaves.deletarChave(diretorio)
            case 9:
                print("SAINDO")
                break
            case 21:
                print("Chave atual")
                print("Chave privada", chavePrivada)
                print("Chave publica", chavePublica)
                


if __name__ == "__main__":
    main()