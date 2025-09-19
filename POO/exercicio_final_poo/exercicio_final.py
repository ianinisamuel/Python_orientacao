from contact import Contact
from contato_agenda import ContactBook

contato_agenda = ContactBook() 
while True:
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Listar Contatos")
    print("4. Buscar Contato")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Nome: ")
        fone = input("Fone: ")
        email = input("Email: ")
        contato = Contact(nome, fone, email)
        contato_agenda.add_contact(contato)
        print("Contato adicionado com sucesso!")

    elif escolha == '2':
        nome = input("Nome do contato a ser removido: ")
        contato_para_remover = None
        for contato in contato_agenda.contacts:
            if contato.name.lower() == nome.lower():
                contato_para_remover = contato
                break
        if contato_para_remover:
            contato_agenda.remove_contact(contato_para_remover)
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

    elif escolha == '3':
        print("Lista de Contatos:")
        contato_agenda.list_contacts()

    elif escolha == '4':
        nome = input("Nome do contato a ser buscado: ")
        print("Resultado da busca:")
        contato_agenda.search_contact(nome)

    elif escolha == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")