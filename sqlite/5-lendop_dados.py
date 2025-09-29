import sqlite3
#1 - Conectando ao BD
connection = sqlite3.connect('aula.db')

# 2 - Criando um cursor
cursor = connection.cursor()

# 3 - Lendo dados da tabela
cursor.execute("SELECT * FROM movies;")
movies = cursor.fetchall()
for movie in movies:
    print(f"ID: {movie[0]}, Nome: {movie[1]}, Ano: {movie[2]}, Nota: {movie[3]}")

#5 Fechando conexão com o BD
connection.close()