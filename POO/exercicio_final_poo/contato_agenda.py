class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def list_contacts(self):
        if not self.contacts:
            print("Nenhum contato na agenda.")  
        else:
            for contact in self.contacts:
                print(contact)
                print("--------------")

    def search_contact(agenda, name):
        for contact in agenda.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return  # retorna apenas se encontrar
    print("Contato não encontrado.")

        