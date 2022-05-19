from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
from typing import Type
import random

class CoffeeMachine():
    def __init__(self):
        self.usage = 0
    class EmptyCup(HotBeverage):
        def __init__(self):
            HotBeverage._init__(self, 0.90, "empty cup")
        def description(self):
            return HotBeverage.description("An empty cup?! Gimme my money back!")
    class BrokenMachineException(Exception):
        def __init__(self):
            Exception.__init__("This coffee machine has to be repaired.")
    def repair(self):
        self.usage = 0
    def serve(self, beverage: Type[HotBeverage]):
        if self.usage != 10:
            if random.choice([True, False]) == True:
                return beverage()
            else:
                return self.EmptyCup()
        else:
            raise self.BrokenMachineException()

a = CoffeeMachine()
print(CoffeeMachine.serve(Coffee()).description())
print(CoffeeMachine.serve(Cappuccino()).description())
print(CoffeeMachine.serve(Chocolate()).description())
print(CoffeeMachine.serve(Tea()).description())
print(CoffeeMachine.serve(Cappuccino()).description())
print(CoffeeMachine.serve(Coffee()).description())
print(CoffeeMachine.serve(Chocolate()).description())
print(CoffeeMachine.serve(Tea()).description())
print(CoffeeMachine.serve(HotBeverage()).description())
print(CoffeeMachine.serve(HotBeverage()).description())
print(CoffeeMachine.serve(Tea()).description())
try:
	print(CoffeeMachine.serve(Coffee()).description())
except Exception as e:
	print(e)
try:
	print(CoffeeMachine.serve(Coffee()).description())
except Exception as e:
	print(e)
CoffeeMachine.rapair()
print(CoffeeMachine.serve(Coffee()).description())
print(CoffeeMachine.serve(Cappuccino()).description())
print(CoffeeMachine.serve(Chocolate()).description())
print(CoffeeMachine.serve(Tea()).description())
print(CoffeeMachine.serve(Cappuccino()).description())
print(CoffeeMachine.serve(Coffee()).description())
print(CoffeeMachine.serve(Chocolate()).description())
print(CoffeeMachine.serve(Tea()).description())
print(CoffeeMachine.serve(HotBeverage()).description())
print(CoffeeMachine.serve(HotBeverage()).description())
print(CoffeeMachine.serve(Tea()).description())
try:
	print(CoffeeMachine.serve(Coffee()).description())
except Exception as e:
	print(e)
try:
	print(CoffeeMachine.serve(Coffee()).description())
except Exception as e:
	print(e)
