class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class Fish(Animal):
    race = ""

class Parrots(Animal):
    color = ""

class Dogs(Animal):
    age = ""

class Zoo:
    def __init__(self):
        self.animals_dict = {}

    def add_animals(self, animal):
        self.animals_dict[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values():
            if animal == category:
                result += 1

        return f"No nosso zoológico temos {result} quantidade de {category}"
    
zoo = Zoo()
peixe = Fish("Nemo", "mamiferos")
print(vars(peixe))
papagaio = Parrots("Louro", "aves")
print(vars(papagaio))
cachorro = Dogs("Mike", "caes")
print(vars(cachorro))

zoo.add_animals(peixe)
zoo.add_animals(papagaio)
zoo.add_animals(cachorro)
print(zoo.total_of_category("aves"))
print(zoo.total_of_category("mamiferos"))
print(zoo.total_of_category("caes"))