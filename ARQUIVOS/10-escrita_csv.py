import csv

name = input("Informe o nome da linguagem que deseja aprender: ")
category = input("Informe a categoria da linguagem: ")

with open("dados/courses.csv", "a", encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, category])