from src.item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_count: int):
        super().__init__(name, price, quantity)
        self.sim_count = sim_count

