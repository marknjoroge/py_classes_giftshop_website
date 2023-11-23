from cart import Cart

class Customer:
    def __init__(self, email, username, password) -> None:
        self.email = email
        self.username = username
        self.password = password
        self.cart = Cart()
        self.account = 0

    def login(self, entered_username, entered_password) -> bool:
        return entered_username == self.username and entered_password == self.password

    def add_to_cart(self, item):
        self.cart.add_item(item)

    def checkout(self) -> float:
        total_bill = self.cart.calculate_total()
        self.account -= total_bill
        return total_bill

    def to_string(self) -> None: 
        print(f"Name: {self.username}, Email: {self.email}, Password: {self.password}, Cart: {self.cart.items}")
