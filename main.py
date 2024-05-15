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
                print("Escolha qual chave importar:")
                print('1- As duas chaves\n2-Somente a chave publica')
                escolha = input("Escolher: ")
                if escolha == '1':
                    carregarChaves.carregar.main(1)
                elif escolha == '2':
                    carregarChaves.carregar.main(2)
                else:
                    print("opcao incorreta! Retornando para o menu principal")
            case 4:
                print("Case 4")
            case 5:
                caminho = 'C:/Users/samue/OneDrive/Área de Trabalho/UFPI/2024.1/segurança/av1/Trabalho/Sistema-de-criptografia/criptografados'
                print("Case 5")
                public_key = carregarChaves.carregar.load_public_key('public_key.pem')
                criptografar.Arquivo('texto.txt', 'criptografados/criptoencrypted_file.enc', public_key) 
                # encrypt_file('path/to/your/file.txt', 'path/to/your/encrypted_file.enc', public_key)
            case 6:
                print("Case 6")
                # Uso
                #private_key = descriptografar.load_private_key('private_key.pem', b'my_strong_password')
                senha = input("Defina a senha para a chave privada: ")
                private_key = carregarChaves.carregar.load_private_key('private_key.pem', senha.encode("utf-8"))
                descriptografar.Arquivo('criptografados/criptoencrypted_file.enc', 'descriptografados/novo.txt', private_key) 
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
