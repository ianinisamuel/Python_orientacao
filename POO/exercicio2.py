class Product:
    def __init__(self, nameProduct, price):
        self.nameProduct = nameProduct
        self.price = price

    def __str__(self):
        return f"Produto: {self.nameProduct} - R$ {self.price} reais"
    
    def discount (self, perc_discount):
        valorDiscount = (self.price/100) * perc_discount
        finalPrice = self.price - valorDiscount
        return int(finalPrice)
    
    
xbox = Product("Xbox One", 4000)
print(xbox)
print(f"O valor total com o desconto é de: R${xbox.discount(20)}")
    