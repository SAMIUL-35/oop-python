# class shop:
#     def __init__(self,name):
#         self.name = name
#         self.cart=[]

#     def add_to_cart(self,item,price,quantity):
#         product={'item':item, 'price':price, 'quantity':quantity}
#         self.cart.append(product)
    
#     def remove_from_cart(self,item):
#         for product in self.cart:
#             if product['item']==item:
#                 self.cart.remove(product)
#                 break

# sami=shop('samiul')
# sami.add_to_cart('mobile','500',5)
# sami.add_to_cart('shirt','400',10)
# print(sami.cart)
# sami.remove_from_cart('mobile')
# print(sami.cart)
class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


p1 = Shop('meh jabeeeen')
p1.add_to_cart('shoes')
p1.add_to_cart('phone')


nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)