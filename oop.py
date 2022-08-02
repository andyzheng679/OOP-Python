class Item:
    pay_rate = 0.8 # 20% off discount
    all =[]
    def __init__(self, name: str, price: float, quantity: int):
        # checks parameter
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)


    def calculate_total_price(self) -> int:
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"



item1 = Item("Phone" , 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 70, 5)

#item2.pay_rate = 0.7

#item1.apply_discount()
#print(item1.price)

#item2.apply_discount()
#print(item2.price)

print(Item.all)

for instance in Item.all:
    print(instance.name)

