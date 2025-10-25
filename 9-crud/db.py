import mysql.connector as s #import a biblioteca

def conexao_banco(): #funcao de conexao
    conexao = s.connect(
        host = 'localhost',          #endereço do banco de dados
        user = 'root',               #usuario           ||
        password =  '',              #senha             ||
        database =  'uala'           #nome              ||
    )
    return conexao

