from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import gerarChaves
import salvarChaves

# Variáveis globais para armazenar as chaves durante a execução do script
private_key = None
public_key = None


def main():
    global private_key, public_key
    while True:
        print("\n=== Sistema de Gerenciamento de Chaves Públicas e Criptografia ===")
        print("1. Gerar Par de Chaves")
        print("2. Exportar Chaves")
        print("3. Importar Chaves")
        print("4. Proteger Chaves")
        print("5. Criptografar arquivos")
        print("6. Descriptografar arquivos")
        print("7. Listar Chaves")
        print("8. Pesquisar Chaves")
        print("9. Apagar Chaves")
        print("10. Sair")
        choice = input("Escolha uma opção: ")

        match int(choice):
            case 1:
                print("Case 1")
                public_key, private_key = gerarChaves.gerar_chaves()
                # print(a)
                # print("----------------------------")
                # print(b)
            case 2:
                if public_key == None:
                    print(
                        "Antes de importar é necessario gerar as cahves. Retorando para o menu principal")
                else:
                    print("Escolha qual chave exportar:")
                    print('1- As duas chaves\n2-Somente a chave publica')
                    escolha = input("Escolher: ")
                    if escolha == '1':
                        salvarChaves.salvarAmbas(public_key, private_key)
                    elif escolha == '2':
                        salvarChaves.salvarPublica(public_key)
                    else:
                        print("opcao incorreta! Retornando para o menu principal")

                
            case 3:
                print("Case 3")
            case 4:
                print("Case 4")
            case 5:
                print("Case 5")
            case 6:
                print("Case 6")
            case 7:
                print("Case 7")
            case 8:
                print("Case 8")
            case 9:
                print("Case 9")
            case 10:
                print("Case 10")


if __name__ == "__main__":
    main()
