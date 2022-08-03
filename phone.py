from item import Item

# inheritance, Item is the parent, Phone is the child
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        # calls super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )
        
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"