import sqlite3
#1 - Conectando ao BD
connection = sqlite3.connect('aula.db')

# 2 - Criando um cursor
cursor = connection.cursor()

# 3 - Solicitando dados do usuário
movie_id = int(input("Digite o ID do filme que deseja atualizar: "))
new_name = input("Digite o novo nome do filme: ")

# 4 - Atualizando dados na tabela
cursor.execute("UPDATE movies SET name = ? WHERE id = ?;", (new_name, movie_id))
connection.commit()

#5 Fechando conexão com o BD
connection.close()