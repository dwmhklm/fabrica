from db import conexao_banco

# nome = 'Jose Maria'
# telefone = '11 94002-8922'
# email = 'jose@maria.com'
# data_nascimento = '1700-01-31'
# senha = 'mariajose123'

nome = str(input("Digite seu nome (ex: José Maria): "))
telefone = str(input("Digite o número do seu telefone (ex: 11 94414-5373): "))
email = str(input("Digite seu email (ex: josemaria@gmail.com): "))
data_nascimento = str(input("Digite sua data de nascimento (ex: 1991-05-25): "))
senha = str(input("Digite sua senha (ex: Senha123): "))


conexao = conexao_banco()

if conexao.is_connected():
    cursor = conexao.cursor()

    sql = """
    INSERT INTO cliente(nome, telefone, email, data_nascimento, senha)
        VALUES(%s, %s, %s, %s, %s)
"""

    dados = (nome, telefone, email, data_nascimento, senha)

    cursor.execute(sql, dados)
    conexao.commit()

    cursor.close()
    conexao.close()

else:
    print("Falha")