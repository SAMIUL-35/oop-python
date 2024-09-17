class shop:
    products =[]
    def __init__(self,name) :
        self.name =name
    def __repr__(self) -> str:
        return f"This shop name is :{self.name}"
    
    def add_product(self,name,price):
        Product=product(name,price)
        self.products.append(Product)
        
class product:
    def __init__(self,name,price) :
        self.name = name
        self.price = price

shop1=shop('test shop')
print(shop1.name)