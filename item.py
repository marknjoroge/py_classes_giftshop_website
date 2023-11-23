class Item:
    def __init__(self, id, description, price, quantityAvailable) -> None:
        self.id = id
        self.description = description
        self.price = price
        self.quantityAvailable = quantityAvailable
        
    def to_string(self) -> None:
        print(f"ID: {self.id}, Description: {self.description}, Price: ${self.price}, Quantity: {self.quantityAvailable}")
