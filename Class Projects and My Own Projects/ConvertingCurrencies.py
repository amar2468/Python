# Use the exchangeratesapi.io to perform currency conversions.
# https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD

import urllib.request
import json

class Currency:

    VALID_CURRENCIES = ['USD', 'EUR', 'GBP', 'AUD', 'CAD',
                    'CNY', 'ILS', 'MXN', 'RUB', 'THB', 'BRL']

    def __init__(self, amount=1, currency_type='EUR'):
        # a quick way of checking for valid currencies
        # for a limited subset of valid currencies
        if currency_type in Currency.VALID_CURRENCIES:
            self.amount = amount
            self.currency_type = currency_type
        else:
            print("Invalid currency type: %s\n", currency_type)
            self.amount = 0
            self.currency_type = ''

    def convert_to(self, new_currency_type):
        if new_currency_type == self.currency_type:
            # nothing to do
            return Currency(self.amount, self.currency_type)

        if new_currency_type not in Currency.VALID_CURRENCIES \
                or self.currency_type not in Currency.VALID_CURRENCIES:
            print("Conversion from {} to {} not allowed".format(self.currency_type, new_currency_type))
            return

        # prepare URL
        url = "https://api.exchangeratesapi.io/latest?base="
        url += self.currency_type
        url += "&symbols=" + new_currency_type
        conv = urllib.request.urlopen(url)
        # read() returns an array of bytes, we want a string decoded in UTF-8
        response = conv.read().decode('UTF-8')
        print(response)

        dictionary1 = {}

        dictionary1 = json.loads(response)

        exchange_amount = dictionary1["rates"][new_currency_type]

        amount = 0
        amount = self.amount * exchange_amount

        print("{} {} => {} {}".format(self.amount, self.currency_type, amount, new_currency_type))
        return Currency(amount, new_currency_type)

    def __str__(self):
        return 'The amount is {} {}'.format(self.amount,self.currency_type)



curr = Currency(7.50, 'USD')
print(curr) # 7.50 USD
curr2 = Currency(2, 'EUR')
print(curr2)  # 2.00 EUR
new_curr = curr2.convert_to(curr.currency_type) # 2.000000 EUR => 2.38 USD
print(new_curr) # 2.38  USD
