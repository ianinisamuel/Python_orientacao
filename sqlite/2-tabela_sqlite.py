import sqlite3

# 1 - Conectando ao BD
connection = sqlite3.connect('aula.db')

# 2 - Criando um cursor
cursor = connection.cursor()

# 3 - Criando uma tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
               );

                """)

# 4 - Fechando a conexão com o BD
print("Tabela criada com sucesso!")
connection.close()  