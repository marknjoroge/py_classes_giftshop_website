from item import Item

class ArabicSweets(Item):
    def __init__(self, item_id, description, price, quantity) -> None:
        super().__init__(item_id, description, price, quantity)