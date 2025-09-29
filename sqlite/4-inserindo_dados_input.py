import sqlite3
#1 - Conectando ao BD
connection = sqlite3.connect('aula.db')

# 2 - Criando um cursor
cursor = connection.cursor()


# 3 - Inserindo dados na tabela via input
name = input("Digite o nome do filme: ")
year = int(input("Digite o ano do filme: "))
score = float(input("Digite a nota do filme: "))
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?);
               """, (name, year, score))

# 4 - Gracando dados no BD
connection.commit()
print("Dados inseridos com sucesso!")

#5 Fechando conexão com o BD
connection.close()