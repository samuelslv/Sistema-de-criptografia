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

# Variáveis globais para armazenar as chaves durante a execução do script
chavePrivada = None
chavePublica = None


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
                chavePublica, chavePrivada = gerarChaves.gerar_chaves()

            case 2:
                if chavePublica == None:
                    print(
                        "Antes de exportar é necessário gerar as cahves. Retornando para o menu principal")
                else:
                    caminho = 'chaves/'
                    print("Escolha qual chave exportar:")
                    print('1-As duas chaves\n2-Somente a chave pública')
                    escolha = input("Escolher: ")
                    if escolha == '1':
                        salvarChaves.salvarAmbas(caminho, chavePublica, chavePrivada)
                    elif escolha == '2':
                        salvarChaves.salvarPublica(caminho, chavePublica)
                    else:
                        print("opção incorreta! Retornando para o menu principal")

            case 3:
                print("Escolha qual chave importar:")
                print('1-As duas chaves\n2-Somente a chave pública')
                escolha = input("Escolher: ")
                if escolha == '1':
                    chavePrivada, chavePublica = carregarChaves.main(1)
                elif escolha == '2':
                    chavePublica = carregarChaves.main(2)
                else:
                    print("opcao incorreta! Retornando para o menu principal")
            case 4:
                chavePublica = carregarChaves.carregarChavePublica('chaves/public_key.pem')
                criptografar.Arquivo('texto.txt', 'criptografados/criptoencrypted_file.enc', chavePublica) 
                
            case 5:
                senha = input("Insira a senha da chave privada: ")
                chavePrivada = carregarChaves.carregarChavePrivada('chaves/private_key.pem', senha.encode("utf-8"))
                descriptografar.Arquivo('criptografados/criptoencrypted_file.enc', 'descriptografados/novo.txt', chavePrivada) 
            case 6:                
                chaves = listarChaves.listar('chaves/', ".pem")
                for chave in chaves:
                    print("Chave encontrada:", chave)
            case 7:
                diretorio = "chaves/"
                termoBuscado = input("Digite o nome da chave para pesquisar: ")
                chaveEncontrada = pesquisarChaves.buscarChave(diretorio, termoBuscado)
                if len(chaveEncontrada) == 0:
                    print("Chave não encontrada")
                else:
                    for chave in chaveEncontrada:
                        print("Chave encontrada:", chave)
            case 8:
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