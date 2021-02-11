#!/usr/bin/python3

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

    def __repr__(self):
        return self.amount,self.currency_type

    def __add__(self, other_curr):
        if type(other_curr) is int or type(other_curr) is float:
            amount_two = self.amount + other_curr
            return Currency(amount_two,self.currency_type)
        elif type(other_curr) is str:
            print("This is not allowed.\n")
            return None
        elif type(other_curr) is Currency:
            if other_curr.currency_type != self.currency_type:
                other_curr = other_curr.convert_to(self.currency_type)
                amount_two = self.amount + other_curr.amount    
            return Currency(amount_two,self.currency_type)

    def __sub__(self, other_curr):
        if type(other_curr) is int or type(other_curr) is float:
            amount_two = self.amount - other_curr
            return Currency(amount_two,self.currency_type)
        elif type(other_curr) is str:
            print("This cannot work.")
            return None
        elif type(other_curr) is Currency:
            if other_curr.currency_type != self.currency_type:
                other_curr = other_curr.convert_to(self.currency_type)
                amount_two = self.amount - other_curr.amount
            return Currency(amount_two,self.currency_type)

    def __radd__(self, other_curr):
        return self.__add__(other_curr)

    def __rsub__(self, other_curr):
        new_curr = Currency(other_curr,self.currency_type)
        return new_curr - self.amount

    def __gt__(self, other_curr):
        if type(other_curr) is int or type(other_curr) is float:
            new_result = self.amount > other_curr.amount
            return Currency(new_result,self.currency_type)
        else:
            if other_curr.currency_type != self.currency_type:
                other_curr = other_curr.convert_to(self.currency_type)

            new_result = self.amount > other_curr.amount
        return new_result


curr = Currency(7.50, 'USD')
print(curr) # 7.50 USD
curr2 = Currency(2, 'EUR')
print(curr2)  # 2.00 EUR
new_curr = curr2.convert_to(curr.currency_type) # 2.000000 EUR => 2.38 USD
print(new_curr) # 2.38  USD
sum_curr = curr + curr2 # 2.000000 EUR => 2.38 USD
print("sum_curr ->",sum_curr) # 9.88 USD
sum_curr2 = curr + 5.5
print("sum_curr2 ->",sum_curr2) # 13.00 USD
sum_curr3 = 10 + curr
print("sum_curr3 ->",sum_curr3) # 17.50 USD

subtract_curr = curr - curr2
print("subtract_curr ->",subtract_curr) # 7.50 - 2.38 = 5.12 USD
subtract_curr2 = curr - 1.5 
print("subtract_curr2 ->",subtract_curr2) # 7.50 - 1.50 = 6.0 USD
subtract_curr3 = 20 - curr2
print(subtract_curr3) # 20 - 2 EUR = 18 EUR

if curr > curr2:
    print("curr is greater than curr2\n")
else:
    print("curr2 is greater than curr\n")
