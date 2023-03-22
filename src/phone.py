from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            return TypeError("Phone")

    # @property
    # def number_of_sim(self):
    #     return f"{self.number_of_sim}"
    # @number_of_sim.setter
    # def number_of_sim(self, number_of_sim):
    #     if number_of_sim <= 0:
    #         raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
