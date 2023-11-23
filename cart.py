from item import Item

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item: Item) -> None:
        self.items[item.id] = item
        print("Added item to cart")

    def calculate_total(self) -> float:
        total = 0
        for item in self.items.values():
            total += item.price * item.quantityAvailable
        return total
    
    def to_string(self) -> None:
        print(f"Items")
        for item in self.items.values():
            print(f"{item.description} {item.price} -> {item.quantityAvailable}")
