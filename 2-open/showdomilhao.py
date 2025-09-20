import os
dicas = ["Sou uma fruta.", "Por dentro sou vermelha e tenho sementes.", "Estou na moda por ai."]

def dica():

    #Duas barras (\\) são usadas porque apenas uma gera conflito com caracteres de escape: \n \r
    hint = open("C:\\Users\\prog3\\Desktop\\dicas.txt", 'r+')

    leia = hint.read()

    if os.stat("C:\\Users\\prog3\\Desktop\\dicas.txt").st_size == 0: #verifica se arquivo está vazio e escreve a primeira dica
        hint.write(dicas[0])
        print("Dica 1")
    elif dicas[0] in leia: #verifica se tem primeira dica no arquivo e escreve a segunda
        hint.seek(0)
        hint.truncate()
        hint.write(dicas[1])
        print("Dica 2")
    elif dicas[1] in leia: #etc
        hint.seek(0)
        hint.truncate()
        hint.write(dicas[2])
        print("Dica 3")
    elif dicas[2] in leia:
         hint.seek(0)
         hint.truncate()
         hint.write("Nao ha mais dicas.")
    hint.close()

try:
    #username = str(input("Digite seu usuário: "))
    username = "prog3"
    desktop = f"C:\\Users\\{username}\\Desktop"
    
    ler = open(f"{desktop}\\senha.txt", 'r')

    if "morango" in ler:
        print(f"{desktop}\\{username}")
        parabens = open(f"{desktop}\\parabens.txt", 'w')
        parabens.write("Parabéns!!!")
        parabens.close()
        ler.close()
        exit
        
    else:
        print("Senha incorreta no arquivo.")
        dica()
        exit
    
except FileNotFoundError:
    print("Não foi possível abrir o arquivo, você digitou o nome do usuário corretamente?")