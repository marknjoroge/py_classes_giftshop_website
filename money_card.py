from item import Item

class MoneyCard(Item):
    def __init__(self, id, description, price, quantityAvailable) -> None:
        super().__init__(id, description, price, quantityAvailable)