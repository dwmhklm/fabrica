NOME_PROGRAMA = "whatsap"

agenda = ["Jorge", "Pedro"]

def cadastro_contato(nome):
    agenda.append(nome)
    print(f"Contato '{nome}' cadastrado com sucesso.")

    
def listar_contatos():
    print("Lista de contatos")
    print(agenda)

def remover_contato():
    contato = input("Qual o contato deseja remover da agenda? ")
    
    if contato not in agenda:
        print("Esse contato não existe.")
    
    else:
        agenda.remove(contato)
        print("{contato} foi removido com sucesso.")

def main():
    while True:
        print("")
        print(NOME_PROGRAMA)

        print("-"*30)
        print("O que você deseja fazer? ")
        print("[1] - Adicionar contato a agenda")
        print("[2] - Listar contatos da agenda")
        print("[3] - Remover contato da agenda")
        print("[4] - Fechar agenda")
        print("-"*30)

        funcao = int(input("Digite o número de acordo com a opção desejada: "))

        if(funcao == 1):
            nome = str(input("Digite o nome do contato a ser adicionado: "))
            cadastro_contato(nome)
        elif(funcao == 2):
            listar_contatos()
        elif(funcao == 3):
            remover_contato()
        elif(funcao == 4):
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()