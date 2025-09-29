import sqlite3
#1 - Conectando ao BD
connection = sqlite3.connect('aula.db')

# 2 - Criando um cursor
cursor = connection.cursor()

#3 - Solicitando dados do usuário
id = int(input("Digite o ID do filme que deseja remover: "))   

# 4 - Removendo dados na tabela
cursor.execute("DELETE FROM movies WHERE id = ?;", (id,))
connection.commit() 

#5 Fechando conexão com o BD
connection.close()