from customer import Customer
from dubai_gift import DubaiGift
from money_card import MoneyCard
from payment import Payment

giftItem1 = MoneyCard('1', 'First money card to be sold online', 599.99, 3)
giftItem2 = DubaiGift('2', 'Black package', 699.99, 1)

paymentOpt1 = Payment()

customer1 = Customer("mail@mail.com", "John Doe", "123pass")
customer2 = Customer("alice@mail.com", "Alice", "alicemail123")

giftItem1.to_string()
customer1.to_string()
customer1.add_to_cart(giftItem1)
paymentOpt1.process_payment(customer1, '78787878787878')

customer1.to_string()
