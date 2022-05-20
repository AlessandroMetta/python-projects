from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random


class CoffeeMachine():

    def __init__(self):
        self.usage = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(0.90, "empty cup")
        def description(self):
            return HotBeverage.description(self, "An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__('This coffee machine has to be repaired.')

    def repair(self):
        self.usage = 0

    def serve(self, beverage):
        if not isinstance(beverage, HotBeverage):
            raise TypeError()
        if self.usage != 10:
            self.usage += 1
            if random.choice([True, False]) == True:
                return beverage
            else:
                return self.EmptyCup()
        else:
            raise self.BrokenMachineException()


def __main__():

    machine = CoffeeMachine()

    print(CoffeeMachine.serve(machine, Coffee()).description())
    print(CoffeeMachine.serve(machine, Cappuccino()).description())
    print(CoffeeMachine.serve(machine, Chocolate()).description())
    print(CoffeeMachine.serve(machine, Tea()).description())
    print(CoffeeMachine.serve(machine, Cappuccino()).description())
    print(CoffeeMachine.serve(machine, Coffee()).description())
    print(CoffeeMachine.serve(machine, Chocolate()).description())
    print(CoffeeMachine.serve(machine, Tea()).description())
    print(CoffeeMachine.serve(machine, HotBeverage()).description())
    print(CoffeeMachine.serve(machine, HotBeverage()).description())

    try:
    	print(CoffeeMachine.serve(machine, Coffee()).description())
    except Exception as e:
    	print(e)
    try:
    	print(CoffeeMachine.serve(machine, Coffee()).description())
    except Exception as e:
    	print(e)

    CoffeeMachine.repair(machine)

    print(CoffeeMachine.serve(machine, Coffee()).description())
    print(CoffeeMachine.serve(machine, Cappuccino()).description())
    print(CoffeeMachine.serve(machine, Chocolate()).description())
    print(CoffeeMachine.serve(machine, Tea()).description())
    print(CoffeeMachine.serve(machine, Cappuccino()).description())
    print(CoffeeMachine.serve(machine, Coffee()).description())
    print(CoffeeMachine.serve(machine, Chocolate()).description())
    print(CoffeeMachine.serve(machine, Tea()).description())
    print(CoffeeMachine.serve(machine, HotBeverage()).description())
    print(CoffeeMachine.serve(machine, HotBeverage()).description())
    
    try:
    	print(CoffeeMachine.serve(machine, Coffee()).description())
    except Exception as e:
    	print(e)
    try:
    	print(CoffeeMachine.serve(machine, Coffee()).description())
    except Exception as e:
    	print(e)


if __name__ == '__main__':
    __main__()