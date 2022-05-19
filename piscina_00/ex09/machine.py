from beverages.py

class CoffeeMachine():
    def __init__(self):

    class EmptyCup(HotBeverage):
        def __init__(self):
            HotBeverage._init__(self, 0.90, "empty cup")
        def description(self):
            return HotBeverage.description("An empty cup?! Gimme my money back!")
    class BrokenMachineException(Exception):
        def __init__(self)
            Exception.__init__("This coffee machine has to be repaired.")
    def repair(self):
    def serve(self, second):
        # check sul tipo di second
        # return: 
