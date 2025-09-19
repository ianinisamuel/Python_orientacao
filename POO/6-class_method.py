"""
1 - O método de classe utiliza o parametreo referente a classe.
2 - O metodo de classe pode acessar ou modificar o estado da classe.
3 - Usamos o decorator @classmethod para criar um método de classe

"""
class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price