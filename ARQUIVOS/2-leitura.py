with open("dados/names.txt", "r", encoding="utf-8") as file:
    for name in file:
        print(f"Olá, {name.strip()}")