import requests as r
import os

os.system('cls') #limpa o terminal

try:
    cep = input("Digite seu CEP: ")
    via_cep = f"https://viacep.com.br/ws/{cep}/json"
    req = r.get(via_cep)

    endereco = req.json()

    rua = endereco['logradouro']
    bairro = endereco['bairro']
    localidade = endereco['localidade']
    estado = endereco['estado']
    regiao = endereco['regiao']
    ddd = endereco['ddd']

    print(f"Rua   : {rua} \nBairro: {bairro} \nCidade: {localidade} ({ddd}) \nEstado: {estado}  \nRegião: {regiao}")

except:
    print("Erro: CEP Inválido/Inexistente")