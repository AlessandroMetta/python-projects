class HotBeverage():
    def __init__(self, p=0.30, n="hot beverage"):
        self.price = p
        self.name = n
    def description(self, des="Just some hot water in a cup"):
        return des 
    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(0.40, "coffee")
    def description(self):
        return HotBeverage.description(self, "A coffee, to stay awake.")

class Tea(HotBeverage):
    def __init__(self):
        super().__init__(n="tea")
    def description(self):
        return HotBeverage.description(self, "Just some hot water in a cup.")

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(0.50, "chocolate")
    def description(self):
        return HotBeverage.description(self, "Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(0.45, "cappuccino")
    def description(self):
        return HotBeverage.description(self, "Un po' di Italia nella sua tazza!")

def __main__():
    a = HotBeverage()
    print(a)
    print()
    a = Coffee()
    print(a)
    print()
    a = Tea()
    print(a)
    print()
    a = Chocolate()
    print(a)
    print()
    a = Cappuccino()
    print(a)
    print()

if __name__ == '__main__':
    __main__()