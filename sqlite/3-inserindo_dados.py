import sqlite3
#1 - Conectando ao BD
connection = sqlite3.connect('aula.db')

# 2 - Criando um cursor
cursor = connection.cursor()

# 3 - Inserindo dados na tabela
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('The Matrix', 1999, 8.7);
               """)

cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Avatar', 2000, 8.2);
               """)

cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Fast and Furious', 1999, 10);
               """)

# 4 - Gracando dados no BD
connection.commit()
print("Dados inseridos com sucesso!")

#5 Fechando conexão com o BD
connection.close()