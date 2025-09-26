from metodos import add_contato, listar_contatos, apagar_contato, buscar_contato

while True:
    print("\n1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Listar Contatos")
    print("4. Buscar Contato")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        add_contato()

    elif escolha == '2':
        apagar_contato()
        pass

    elif escolha == '3':
        listar_contatos()

    elif escolha == '4':
        buscar_contato()
        pass

    elif escolha == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")
