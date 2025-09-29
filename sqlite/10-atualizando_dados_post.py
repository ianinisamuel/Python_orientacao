from conexao_post import comn   

cursor_obj = comn.cursor()

sql = """ UPDATE games
                SET name = %s
                WHERE id = %s"""
                
cursor_obj.execute(sql, ("cs2 23", 6))

comn.commit()

comn.close()