from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
from typing import Type
import random

class CoffeeMachine():
    def __init__(self):
        self.usage = 0
    class EmptyCup(HotBeverage):
        def __init__(self):
            HotBeverage.__init__(self, 0.90, "empty cup")
        def description(self):
            return HotBeverage.description(self, "An empty cup?! Gimme my money back!")
    class BrokenMachineException(Exception):
        def __init__(self):
            Exception.__init__(self, 'This coffee machine has to be repaired.')
    def repair(self):
        self.usage = 0
    def serve(self, beverage: Type[HotBeverage]):
        if self.usage != 10:
            self.usage += 1
            if random.choice([True, False]) == True:
                return beverage
            else:
                return self.EmptyCup()
        else:
            raise self.BrokenMachineException()

def __main__():
    a = CoffeeMachine()
    print(CoffeeMachine.serve(a, Coffee()).description())
    print(CoffeeMachine.serve(a, Cappuccino()).description())
    print(CoffeeMachine.serve(a, Chocolate()).description())
    print(CoffeeMachine.serve(a, Tea()).description())
    print(CoffeeMachine.serve(a, Cappuccino()).description())
    print(CoffeeMachine.serve(a, Coffee()).description())
    print(CoffeeMachine.serve(a, Chocolate()).description())
    print(CoffeeMachine.serve(a, Tea()).description())
    print(CoffeeMachine.serve(a, HotBeverage()).description())
    print(CoffeeMachine.serve(a, HotBeverage()).description())
    try:
    	print(CoffeeMachine.serve(a, Coffee()).description())
    except Exception as e:
    	print(e)
    try:
    	print(CoffeeMachine.serve(a, Coffee()).description())
    except Exception as e:
    	print(e)
    CoffeeMachine.repair(a)
    print(CoffeeMachine.serve(a, Coffee()).description())
    print(CoffeeMachine.serve(a, Cappuccino()).description())
    print(CoffeeMachine.serve(a, Chocolate()).description())
    print(CoffeeMachine.serve(a, Tea()).description())
    print(CoffeeMachine.serve(a, Cappuccino()).description())
    print(CoffeeMachine.serve(a, Coffee()).description())
    print(CoffeeMachine.serve(a, Chocolate()).description())
    print(CoffeeMachine.serve(a, Tea()).description())
    print(CoffeeMachine.serve(a, HotBeverage()).description())
    print(CoffeeMachine.serve(a, HotBeverage()).description())
    try:
    	print(CoffeeMachine.serve(a, Coffee()).description())
    except Exception as e:
    	print(e)
    try:
    	print(CoffeeMachine.serve(a, Coffee()).description())
    except Exception as e:
    	print(e)

if __name__ == '__main__':
    __main__()