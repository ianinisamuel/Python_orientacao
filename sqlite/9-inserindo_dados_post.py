from conexao_post import comn

cursor_obj = comn.cursor()

games = [
    ("The Legend of Zelda: Ocarina of Time", 2024, 5),
    ("Super Mario 64", 2019, 7),
]

for game in games:
  cursor_obj.execute("INSERT INTO games (name, year, score)"
  "VALUES (%s, %s, %s)", game) 

comn.commit()  
comn.close()