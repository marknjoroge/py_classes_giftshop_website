class Payment:
    def process_payment(self, customer, credit_card) -> None:
        if self.validate_credit_card(credit_card):
            total_bill = customer.checkout()
            print(f"Payment successful! Total bill: ${total_bill}")
        else:
            print("Invalid credit card. Payment failed.")

    def validate_credit_card(self, credit_card) -> bool:
        return True

