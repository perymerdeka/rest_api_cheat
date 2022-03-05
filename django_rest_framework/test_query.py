# test database query with dummy data

from finance.models import Transaction
import random
from decimal import Decimal
from finance.models import Currency, Category

data_list: list = []
currencies = list(Currency.objects.all())
categories = list(Category.objects.all())

for i in range(1, 100000):
    data_tx = Transaction(amount=random.randrange(Decimal(i), Decimal(100000)), currency=random.choice(currencies), description="", category=random.choice(categories))
    data_list.append(data_tx)

# append data
Transaction.bulk_create(data_list)
