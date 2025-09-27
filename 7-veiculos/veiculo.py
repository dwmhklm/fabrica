import csv
import json
import os

dados = "C:\\Users\\Prog3\\Desktop\\gbn\\clone\\fabrica\\7-veiculos\\veiculos.csv" #endereço do arquivo CSV
dados_json = "C:\\Users\\Prog3\\Desktop\\gbn\\clone\\fabrica\\7-veiculos\\veiculos.json"
veiculos = []

with open(dados, "r", encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=",")
    
    for linha in leitor:
        veiculos.append(linha)

with open(dados_json, "w", encoding='utf-8') as arquivo_json:
    json.dump(veiculos, arquivo_json, indent=2, ensure_ascii=False)