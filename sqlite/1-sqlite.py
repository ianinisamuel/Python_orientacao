import sqlite3

# 1 - Criando o BD
connection = sqlite3.connect('aula.db')

# 2 - Verifica se houve alterações na base de dados
print(connection.total_changes)