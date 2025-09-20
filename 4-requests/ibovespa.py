import requests as r

awesome = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

requisicao = r.get(awesome)

dolar_real = float(requisicao.json()['USDBRL']['bid'])
euro_real = float(requisicao.json()['EURBRL']['bid'])
bitcoin_real = float(requisicao.json()['BTCBRL']['bid'])

print("-"*30)
print("Selecione o tipo de conversão:")
print("1- BRL/USD")
print("2- USD/BRL")
print("3- BRL/EUR")
print("4- EUR/BRL")
print("5- BRL/BTC")
print("6- BTC/BRL")
print("0- Sair")
print("-"*30)
escolha = int(input(""))

if(escolha == 1):
    valor = float(input("Digite o valor em Real (R$) "))
    print(f"R${valor} é igual a ${valor / dolar_real:.2f}")
elif(escolha == 2):
    valor = float(input("Digite o valor em Dólar ($) "))
    print(f"${valor} é igual a ${valor * dolar_real:.2f}")
elif(escolha == 3):
    valor = float(input("Digite o valor em Real (R$) "))
    print(f"R${valor} é igual a €{valor / euro_real:.2f}")
elif(escolha == 4):
    valor = float(input("Digite o valor em Euro (R$) "))
    print(f"€{valor} é igual a R${valor * euro_real:.2f}")
elif(escolha == 5):
    valor = float(input("Digite o valor em Real (R$) "))
    print(f"R${valor} é igual a ₿{valor / bitcoin_real:.8f}")
elif(escolha == 6):
    valor = float(input("Digite o valor em Bitcoin (₿) "))
    print(f"₿{valor} é igual a R${valor * bitcoin_real:.2f}")
elif(escolha == 0):
    exit
else:
    print("Escolha inválida")

