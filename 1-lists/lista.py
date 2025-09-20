nomes = ["Joaquim", "Maria", "Ana"]

nomes.append("João")
nomes.append("Bob")

while True:
    nome = input("Digite um nome (ou digite EXIT / pressione Enter para sair): ").upper()
    if nome == "EXIT" or nome == "":
        break
    nomes.append(nome)
    

qntd = len(nomes)

for i in range(qntd):
    print(nomes[i])
