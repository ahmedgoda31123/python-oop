import csv

class Item:
    pay_rate = 0.8 # The pay rate after discount
    all = []

    def __init__(self, name: str, price: float, quantity = 0):    
        # Validate the received arguments
        assert price >= 0, f"Price {price} should be >= 0"
        assert quantity >= 0, f"Quantity {quantity} should be >= 0"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_dicount(self):
        self.__price = self.__price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"

    @classmethod
    def instantiate_from_csv(cls):
        with open('main.csv', 'r') as f:
            reader = csv.DictReader(f)
            Items = list(reader)
        for _Item in Items:
            Item(
               name=_Item.get('name'),
               price=float(_Item.get('price')),
               quantity=int(_Item.get('quantity')),
            ) 
    
    @staticmethod
    def is_integer(num):
        # 5.0 will be encountered an int
        if (isinstance(num, float)): 
            return num.is_integer()
        elif (isinstance(num, int)):
            return True
        else:
            return False
    
    # Getter
    @property
    def name(self):
        return self.__name 

    # Setter
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Then name is too long")
        else:
            self.__name = value   

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if value < 0:
            raise Exception("Price can't be negative") 
        else:
            self.__price = value

    def __private_method(self):
        pass