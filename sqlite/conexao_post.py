import psycopg2

comn = psycopg2.connect(
    database="fliperama",
    user="postgres",
    password="admin",
    host="localhost",
    port = "5432"
)