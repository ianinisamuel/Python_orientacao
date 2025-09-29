from conexao_post import comn

cursor_obj = comn.cursor()

cursor_obj.execute("SELECT * FROM games")

result = cursor_obj.fetchall()

print(result)