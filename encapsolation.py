class shop:
    products =[]
    def __init__(self,name,balance) :
        self.name =name
        self.__balance =balance
    def __repr__(self) -> str:
        return f"This shop name is :{self.name} and :{self.balance}"
    
    def add_product(self,name,price):
        Product=product(name,price)
        self.products.append(Product)
    def sell(self,amount):
        self.__balance=self.__balance +amount

class product:
    def __init__(self,name,price) :
        self.name = name
        self.price = price

shop1=shop('test shop',500)
print(shop1)
shop1.balance=0
print(shop1)