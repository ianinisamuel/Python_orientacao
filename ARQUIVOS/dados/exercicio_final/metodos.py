def add_contato():
    name = input("Digite o nome:\n")
    contato = input("Digite o contato:\n")
    """
    - Arquivos:
    1 - opção w - write (escrita)
    2 - opção r - read (leitura)
    3 - opção a - append (acrescentar)
    """
    with open(r"c:\Python\ARQUIVOS\dados\exercicio_final\contatos.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}\n")
        file.write(f"{contato}\n")

def listar_contatos():
    contatos = []
    with open(r"c:\Python\ARQUIVOS\dados\exercicio_final\contatos.txt", "r", encoding="utf-8") as file:
        linhas = file.readlines()
        for i in range(0, len(linhas), 2):
            nome = linhas[i].strip()
            contato = linhas[i + 1].strip() if i + 1 < len(linhas) else ""
            contatos.append({"nome": nome, "contato": contato})
    
    print(f"{'Nome':<20} {'Contato'}")
    print("-" * 30)
    for c in contatos:
        print(f"{c['nome']:<20} {c['contato']}")


def apagar_contato():
    nome_para_remover = input("Digite o nome do contato a ser removido:\n")
    contatos = []
    contato_encontrado = False

    with open(r"c:\Python\ARQUIVOS\dados\exercicio_final\contatos.txt", "r", encoding="utf-8") as file:
        linhas = file.readlines()
        for i in range(0, len(linhas), 2):
            nome = linhas[i].strip()
            contato = linhas[i + 1].strip() if i + 1 < len(linhas) else ""
            if nome.lower() != nome_para_remover.lower():
                contatos.append({"nome": nome, "contato": contato})
            else:
                contato_encontrado = True

    if contato_encontrado:
        with open(r"c:\Python\ARQUIVOS\dados\exercicio_final\contatos.txt", "w", encoding="utf-8") as file:
            for c in contatos:
                file.write(f"{c['nome']}\n")
                file.write(f"{c['contato']}\n")
        print("Contato removido com sucesso.")
    else:
        print("Contato não encontrado.")


def buscar_contato():
    nome_para_buscar = input("Digite o nome do contato a ser buscado:\n")
    contatos_encontrados = []

    with open(r"c:\Python\ARQUIVOS\dados\exercicio_final\contatos.txt", "r", encoding="utf-8") as file:
        linhas = file.readlines()
        for i in range(0, len(linhas), 2):
            nome = linhas[i].strip()
            contato = linhas[i + 1].strip() if i + 1 < len(linhas) else ""
            if nome_para_buscar.lower() in nome.lower():
                contatos_encontrados.append({"nome": nome, "contato": contato})

    if contatos_encontrados:
        print(f"{'Nome':<20} {'Contato'}")
        print("-" * 30)
        for c in contatos_encontrados:
            print(f"{c['nome']:<20} {c['contato']}")
    else:
        print("Nenhum contato encontrado.")