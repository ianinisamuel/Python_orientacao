with open("dados/courses.csv","r", encoding=("utf-8")) as file:
    for line in file:
        # row = line.strip().split(",")
        # print(f"Curso: {row[0]} - Especialidade: {row[1]}")
        language, category = line.strip().split(",")
        print(f"{language} - {category}")