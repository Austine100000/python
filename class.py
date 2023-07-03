class fruits:
    def __init__(self, type, color, price,shape):
        self.fruittype = type
        self.fruitcolor = color
        self.fruitprice = price
        self.fruitshape = shape

    def display(self):
        print(self.fruittype, self.fruitcolor, self.fruitprice, self.fruitshape)


myobj = fruits("Apple", "Red", "50", "circle")
myobj.display()


class car:
    def __init__(self, type, color, year):
        self.cartype = type
        self.carcolor = color
        self.caryear =year

    def display(self):
        print(self.cartype, self.carcolor, self.caryear)


myobj2 = car("Audi", "Black", "2023")
myobj2.display()

class people:
    def__init__()