from item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal 0"
        assert broken_phones <= quantity, f"Number of Broken Phones {broken_phones} can't be greater than Quantity {quantity}"

        self.broken_phones = broken_phones
