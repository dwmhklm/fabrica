import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "escola"
)

cursor = conexao.cursor()

def inserir_aluno(nome, idade, email):
    sql = "INSERT INTO alunos (nome, idade, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, idade, email))
    conexao.commit()
    print("Aluno inserido com sucesso")

def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    for linha in cursor.fetchall():
        print(linha)

def deletar_alunos(id):
    sql = "DELETE FROM alunos WHERE id=%s"
    cursor.execute(sql, id)
    conexao.commit()
    print("Aluno deletado com sucesso")

def atualizar_aluno(id, novo_nome, nova_idade, novo_email):
    sql = "UPDATE alunos SET nome=%s, idade=%s, email=%s WHERE id=%s"
    cursor.execute(sql,(id, novo_nome, nova_idade, novo_email))
    conexao.commit()
    print("Aluno atualizado com sucesso")

if __name__ == "__main__":
    # inserir_aluno("Gabriel", 67, "gab@riel.com")
    atualizar_aluno(4, "nao sei", 20, "naosei@gmail.com")   


cursor.close()
conexao.close()
