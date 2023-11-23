
class Sale:
    def __init__(self, item, date, buyer) -> None:
        self.item = item
        self.date = date
        self.buyer = buyer
        
    def to_string(self) -> None:
        print(f"Item: {self.item.to_string()}, Date: {self.date}, Buyer: ${self.buyer}")
    