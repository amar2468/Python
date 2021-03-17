# This project allows the user to enter a value and a currency. Then, the user has the ability to ask the program to convert that currency
# entered into the new currency they specified. This program uses an API to get the latest exchange rate. 

# Use the exchangeratesapi.io to perform currency conversions.
# https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD

import urllib.request
import json

class Currency:

    VALID_CURRENCIES = ['USD', 'EUR', 'GBP', 'AUD', 'CAD']

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

        print("{} {} => {:.2f} {}".format(self.amount, self.currency_type, amount, new_currency_type))
        return Currency(amount, new_currency_type)

    def __str__(self):
        return 'The amount is {:.2f} {}'.format(self.amount,self.currency_type)



counter = 1

while counter == 1:
    print("Welcome to the Currency Exchange program that uses an API!")
    print("1.Enter a value and currency and exchange it: ")
    print("2.Exit the program: ")

    option_selected = int(input("Enter either option 1 or 2: "))
    if option_selected == 1:
        value_entered = int(input("Enter the value you wish to convert: "))
        currency_chosen = input("Enter the currency type from the following: \n"
                        "1. USD\n"
                        "2. EUR\n"
                        "3. GBP\n"
                        "4. AUD\n"
                        "5. CAD\n")
        if currency_chosen == "USD":
            currency_chosen = "USD"
            value_and_curreny = Currency(value_entered, 'USD')
            new_value_with_currency_returned = value_and_curreny.convert_to("EUR")
            print(new_value_with_currency_returned)
        elif currency_chosen == "EUR":
            currency_chosen = "EUR"
            value_and_curreny = Currency(value_entered, 'EUR')
            new_value_with_currency_returned = value_and_curreny.convert_to("USD")
            print(new_value_with_currency_returned)
        elif currency_chosen == "GBP":
            currency_chosen = "GBP"
            value_and_curreny = Currency(value_entered, 'GBP')
            new_value_with_currency_returned = value_and_curreny.convert_to("CAD")
            print(new_value_with_currency_returned)
        elif currency_chosen == "AUD":
            currency_chosen = "AUD"
            value_and_curreny = Currency(value_entered, 'AUD')
            new_value_with_currency_returned = value_and_curreny.convert_to("GBP")
            print(new_value_with_currency_returned)
        elif currency_chosen == "CAD":
            currency_chosen = "CAD"
            value_and_curreny = Currency(value_entered, 'CAD')
            new_value_with_currency_returned = value_and_curreny.convert_to("AUD")
            print(new_value_with_currency_returned)
        
        else:
            currency_chosen = ""
            print("Incorrect currency entered: Back to main menu: ")
        
    elif option_selected == 2:
        print("Thanks for using the program!")
        counter = 0
    else:
        print("\nIncorrect option selected! Returning back to main menu...\n")
