class Item:
    def __init__(self, name, price, weidht):
        self.name = name
        self.price = price 
        self.weidht = weidht

    # для левого сложения

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other
        return self.price + other.price
    
    # для правого сложения

    def __radd__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):            
            return self.price + other
        return self.price + other.price



item1 = Item("Проццессор", 15_000, 0.3)
item2 = Item("Видюха", 30_000, 0.8)

# result = item1.price + item2.price
# result = item1 + item2

# правое сложение

result = 1000 + item1

# левое сложение

result = item1 + 1000
print(result)

        