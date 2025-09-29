from conexao_post import comn

cursor_obj = comn.cursor()

sql = """ DELETE FROM games
            WHERE id = %s"""
                
cursor_obj.execute(sql, (6,))

comn.commit()

comn.close()