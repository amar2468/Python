# Create a program that manages an online shopping cart. The user can choose between being a loyal, bargain hunter or needs based customer.
# The user can add items to the shopping cart and can see the list of products depending on what type of customer they are.
# Author: Amar Plakalo
# Date 17/12/2020 - Updated 17/03/2021
# Used Visual Studio Code on Windows 10

import urllib.request
import json

class ShoppingCart:
    """This class is a shopping cart that can have items added to it or removed from it and it can display the checkout"""
    def __init__(self,dictionary_of_products:dict,user_shopping_cart:dict):
        """This is the __init__ method that receives arguments initialises the variables inside the ShoppingCart class"""
        self.dictionary_of_products = dictionary_of_products
        self.user_shopping_cart = user_shopping_cart
    def adding_products(self,item_number:int):
        """This method is there so that items can be added to the shopping cart of the user. It receives the argument item_number which is the item number the user wants to add"""
        list_of_keys = list(self.dictionary_of_products) # Convert the list of products from a dictionary to a list so I can access the key
        try: # attempt to do this
            key_needed = list_of_keys[item_number - 1] # whatever item number the user chose gets subtracted by 1 so that the first element index is not 0 but 1
        except IndexError: # if the index entered does not exist
            print("The element number you chose does not exist. Try another one.") # error message
        else: # if everything goes well
            list_of_values = self.dictionary_of_products.values() # put the values inside the list_of_values 
            values_in_dict = list(list_of_values) # this makes sure that the values are in a list
        
            value_needed = values_in_dict[item_number - 1] # whatever item number the user chose gets subtracted by 1 so that the first element index is not 0 but 1
        
            self.user_shopping_cart[key_needed] = value_needed # creates a key:value inside the user's shopping cart

    def removing_products(self,item_number:int):
        """The role of this method is to remove products from the user shopping cart. It receives an argument item_number which is the item number the user wants to get rid of"""
        list_of_keys = list(self.dictionary_of_products) # Convert the dict of products from a dictionary to a list so I can access the key
        try: # try this
            key_needed = list_of_keys[item_number - 1] # whatever item number the user chose gets subtracted by 1 so that the first element index is not 0 but 1
        except IndexError: # if everything goes well
            print("Item number chosen does not exist. Try a different one") # error message
        else: # if everything goes well
            if key_needed in self.user_shopping_cart:
                self.user_shopping_cart.pop(key_needed) # remove the item from the shopping cart of the user
            elif key_needed not in self.user_shopping_cart:
                print("Key is not inside the shopping cart. Do it again.")
    def display_shopping_cart(self):
        """This method's job is to return the shopping cart from the user so that it can be shown to the user"""
        return '{}'.format(self.user_shopping_cart) # shows the shopping cart of the user
    def perform_checkout(self,curr_type:str):
        """This method makes sure that the shopping cart is not empty and adds up the total and returns it to the user"""
        total = 0 # this is used to calculate the total of the transaction
        if self.user_shopping_cart == {}: # if nothing was added to the shopping cart
            print("You cannot checkout because you have no products in your shopping cart\n") # error message
            continue_shopping = 0 # set continue_shopping to 0 so that it can be returned back and for the menu to reappear
            return continue_shopping # return the value
        else: # if it is not empty
            for value in self.user_shopping_cart.values(): # iterate over the values
                total = total + value # add the value to the current total and store in the total variable
            total = round(total,2) # round to two decimal places
        print("The total amount due is",total,curr_type) # print message that shows the price and the currency
        customer_response = input("Are you happy with the amount due and the products that you have added in your shopping cart? Say either y for yes or n for no: ")
        if customer_response.startswith('y') or customer_response.startswith('Y'): # if user chooses y
            print("Thank you for shopping in our online store! Goodbye!!") # prints a thank you message
        elif customer_response.startswith('n') or customer_response.startswith('N'): # if they choose no
            print("Ok. Continue shopping!!") # prompts them to continue to shop
            continue_shopping = 0 # this makes sure that the user will return back to the main menu
            return continue_shopping # return the value
        else: # if y or no is not selected
            print("You haven't selected the correct option. You are going to be redirected back to the main menu") # tell the user
            continue_shopping = 0 # this makes sure that the user will return back to the main menu
            return continue_shopping # return the value
    def __str__(self):
        """The __str__ method prints the products that are available depending on the customer type chosen"""
        return 'These are the products we have for you: {}'.format(self.dictionary_of_products)
class CustomerClass:
    """This class represents the customer and it initialises some variables and uses private attributes along with printing instances"""
    def __init__(self,name:str,surname:str,country:str,mobile:str):
        """Receives arguments and initialises the variables from the class"""
        self.name = name
        self.surname = surname
        self.country = country
        self._mobile = mobile
    def get_mobile(self):
        """get_mobile method returns the user the mobile phone number that they entered. This method is needed because mobile is private"""
        return self._mobile # returns the private attribute
    def set_mobile(self,mobile):
        """This sets the variable mobile using the argument that is passed to the method"""
        self._mobile = mobile # makes mobile a private attribute
    def __str__(self):
        """Prints the instances of the name, surname and the country of the user to the screen"""
        info_about_details = "The name is " + str(self.name) + " and the surname is " + str(self.surname) + ". The country is " + str(self.country)
        return info_about_details
class LoyalCustomers(CustomerClass):
    """This is a subclass of the CustomerClass and it represents one type of customer which is loyal"""
    def __init__(self,name:str,surname:str,country:str,mobile:str,customer_type:str,loyal_customers_dict_of_product:dict,user_shopping_cart:dict):
        """The constructor initialises variables and inherits attributes from the CustomerClass that may be needed"""
        self.customer_type = customer_type
        self.loyal_customers_dict_of_product = loyal_customers_dict_of_product
        self.customer_type = 'Loyal Customer' # sets the customer type to loyal customer
        CustomerClass.__init__(self,name,surname,country,mobile) # inherits attributes from CustomerClass
    def currency_conversions(self,currency_picked:str,user_shopping_cart:dict,loyal_customers_dict_of_product:dict,type_currency:str):
        """This method converts the currency if the user wants to i.e. if they choose dollars."""
        if currency_picked.startswith('e') or currency_picked.startswith('E'): # if user chooses euro
            type_currency = 'EUR' # set currency to euro
        elif currency_picked.startswith('d') or currency_picked.startswith('D'): # if user chose dollars
            url = "https://api.exchangeratesapi.io/latest?base="
            url += "EUR"
            url += "&symbols=" + "USD"
            conv = urllib.request.urlopen(url)

            response = conv.read().decode('UTF-8')
            print(response)

            dictionary1 = {}

            dictionary1 = json.loads(response)

            exchange_amount = dictionary1["rates"]["USD"]

            for key,value in loyal_customers_dict_of_product.items(): # iterate over key,value in loyal customer list of products
                value = value * exchange_amount
                value = round(value,2) # round to two decimal places
                loyal_customers_dict_of_product[key] = value # put price into dictionary in place of the old price
            type_currency = 'DOLLARS' # sets currency to dollars
        return type_currency # returns the currency so that when checkout is performed, a currency is displayed
    def __str__(self):
        """This method prints the type of the customer that the user is, which in this case is a loyal customer"""
        return "You are a " + self.customer_type # prints what customer type the user is
class BargainHunters(CustomerClass):
    """This is a subclass of the CustomerClass and it represents the bargain hunter"""
    def __init__(self,name:str,surname:str,country:str,mobile:str,customer_type:str,bargain_hunter_dict_of_products:dict,user_shopping_cart:dict):
        """The constructor initialises variables and inherits attributes from CustomerClass"""
        self.customer_type = customer_type
        self.bargain_hunter_dict_of_products = bargain_hunter_dict_of_products 
        self.customer_type = 'Bargain Hunter' # set customer type to bargain hunter
        CustomerClass.__init__(self,name,surname,country,mobile) # inherit attributes from CustomerClass
    def bargain_hunter_currency_options(self,currency_picked:str,user_shopping_cart:dict,bargain_hunter_dict_of_products:dict,type_currency:str):
        """This method performs any currency conversion necessary so that the user pay in the correct currency and see the correct price"""
        if currency_picked.startswith('e') or currency_picked.startswith('E'): # if user chose euro
            type_currency = 'EUR' # set currency to euro
        elif currency_picked.startswith('d') or currency_picked.startswith('D'): # if user chose dollars
            url = "https://api.exchangeratesapi.io/latest?base="
            url += "EUR"
            url += "&symbols=" + "USD"
            conv = urllib.request.urlopen(url)

            response = conv.read().decode('UTF-8')
            print(response)

            dictionary1 = {}

            dictionary1 = json.loads(response)

            exchange_amount = dictionary1["rates"]["USD"]


            for k,val in bargain_hunter_dict_of_products.items(): # iterate over key,value in list of products of bargain hunters
                val = val * exchange_amount # multiply price by exchange rate
                val = round(val,2) # round to 2 decimal places
                bargain_hunter_dict_of_products[k] = val # put new value into dictionary in place of the old one
            type_currency = 'DOLLARS' # sets currency to dollars
        else:
            type_currency = 'EUR' # This is the default currency if the user doesn't correctly choose euro or dollar
        return type_currency # returns the currency so that when checkout is performed, a currency is displayed
    def __str__(self):
        """This method prints the customer type which is a bargain hunter"""
        return "You are a " + self.customer_type # prints what customer type the user is
class NeedBased(CustomerClass):
    """This is a subclass from the CustomerClass and it represents the needs based customer"""
    def __init__(self,name:str,surname:str,country:str,mobile:str,customer_type:str,need_based_customers_dict_of_products:dict,user_shopping_cart:dict):
        """This constructor takes the arguments passed to it and initialises the variables. The attributes from CustomerClass are inherited"""
        self.customer_type = customer_type 
        self.need_based_customers_dict_of_products = need_based_customers_dict_of_products
        self.customer_type = 'Need Based Customer' # this will show the user what customer type they are
        CustomerClass.__init__(self,name,surname,country,mobile) # Inheriting attributes from CustomerClass
    def need_based_currency_options(self,currency_picked:str,user_shopping_cart:dict,need_based_customers_dict_of_products:dict,type_currency:str):
        """This method converts the currency if needed so the user can see what price they are supposed to pay for an item"""
        if currency_picked.startswith('e') or currency_picked.startswith('E'): # if euro is picked, execute this
            type_currency = 'EUR' # set currency to euro
        elif currency_picked.startswith('d') or currency_picked.startswith('D'): # if user chooses dollars

            url = "https://api.exchangeratesapi.io/latest?base="
            url += "EUR"
            url += "&symbols=" + "USD"
            conv = urllib.request.urlopen(url)

            response = conv.read().decode('UTF-8')
            print(response)

            dictionary1 = {}

            dictionary1 = json.loads(response)

            exchange_amount = dictionary1["rates"]["USD"]


            for k,val in need_based_customers_dict_of_products.items(): # iterate over key,value in list of products from need based customers
                val = val * exchange_amount # multiply the price of the product by the exchange rate
                val = round(val,2) # round it to two decimal places
                need_based_customers_dict_of_products[k] = val # put that value into the dictionary
            type_currency = 'DOLLARS' # if the user chose dollars, the currency type is set to dollars
        else:
            type_currency = 'EUR' # This is the default currency if the user doesn't correctly choose euro or dollar
        return type_currency # returns the currency type so that when the user wants to perform checkout, a currency is shown along with the price
    def __str__(self):
        """Method that shows the type of customer that the user is, which in this case is a needs based customer"""
        return "You are a " + self.customer_type # prints what customer type the user is

def menu(): # This is the menu that will present the user with options regarding the online shopping.
    menu_choice = 0 # this records the menu option in the program

    i = 0 # this variable is set to 0 at the start and the value of the variable would change depending on the type of customer you are e.g. if you picked loyal, i = 1. This is used so that I can call the instances correctly depending on what the user chose.

    use_option1_first = 0 # this is used so that once a customer is created, the user cannot create one again.

    type_of_currency = '' # string that is empty and can be assigned EUR or DOLLARS depending on the user's choice

    bargain_hunter_dict_of_products = {'Lenovo IdeaPad':300,'Sony Bravia tv':240,'LG tablet':150,'alarm':30,'Huawei P30 Lite':180}

    loyal_customers_dict_of_product = {'iPhone 12 Pro Max':1400,'Samsung Galaxy Note20 Ultra 5G':1349,'rolex':6000,'gucci t-shit':1422}

    need_based_customers_dict_of_products = {'Hp Laptop':450,'Asus Laptop':530,'Acer Laptop':600,'Dell Laptop':800}

    user_shopping_cart = {} # This is the user's shopping cart which is initially empty and they can add items from whatever list that they have chosen i.e. what customer they are

    while menu_choice != 1 and menu_choice != 2 and menu_choice != 3 and menu_choice != 4 and menu_choice != 5: # makes sure the menu loops
        print("Welcome to our online shop! Choose an option from the menu: ")
        print("1.Create a Customer: ")
        print("2.List Products: ")
        print("3.Add/Remove a Product to the Shopping Cart: ")
        print("4.See Current Shopping Cart: ")
        print("5.Checkout: ")

        # This try/except block is present in case the user enters an option that does not exist
        try:
            menu_choice = int(input("Enter an option from 1-5\n"))
        except ValueError:
            print("You did not choose an option from 1-6. Enter your option again, please!")
        else: # if everything goes well i.e. correct option entered
            if menu_choice == 1 and use_option1_first == 0: # if the user chose menu option 1 and if they never picked option 1 before
                f_name = input("Enter your first name: ")
                s_name = input("Type in your surname: ")
                your_country = input("Input your country: ")
                mobile_number = input("Enter phone number: ")
                currency_chosen = input("Do you want to use euros or dollars? Type e for euro or d for dollars: ")
                if i == 0: # if the user is using option 1 currently
                    type_of_customer = input("If you are a loyal customer, enter l. if you are a bargain hunter, enter b. If you are a need based customer, enter n: ")
                    if type_of_customer.startswith('l') or type_of_customer.startswith('L'): # This is executed if the user chooses loyal customer
                        person_details = CustomerClass(f_name,s_name,your_country,mobile_number) # calls CustomerClass and sends variables to it
                        customer_loyal = LoyalCustomers(f_name,s_name,your_country,mobile_number,type_of_customer,loyal_customers_dict_of_product,user_shopping_cart) # calls LoyalCustomers and sends the variables to it
                        type_of_currency = LoyalCustomers(f_name,s_name,your_country,mobile_number,type_of_customer,loyal_customers_dict_of_product,user_shopping_cart).currency_conversions(currency_chosen,user_shopping_cart,loyal_customers_dict_of_product,type_of_currency) # This calls the method inside the LoyalCustomers subclass which converts the currency if needed
                        print(person_details) # prints the persons details returned from the CustomerClass
                        print(person_details.get_mobile()) # prints the persons details that are private inside the get_mobile method in the CustomerClass
                        print(customer_loyal) # prints the details in LoyalCustomer subclass
                        i = 1 # sets i to 1 meaning that once this option is done, the program will know that the user is that particular customer
                        use_option1_first = 1 # this is set to 1 so that option 1 cannot be done again once it is done once
                    elif type_of_customer.startswith('b') or type_of_customer.startswith('B'): # This is executed if the user chooses bargain hunter customer
                        person_details = CustomerClass(f_name,s_name,your_country,mobile_number) # calls CustomerClass and sends variables to it
                        customer_bargain = BargainHunters(f_name,s_name,your_country,mobile_number,type_of_customer,bargain_hunter_dict_of_products,user_shopping_cart) # calls BargainHunters and passes the variables to it
                        type_of_currency = BargainHunters(f_name,s_name,your_country,mobile_number,type_of_customer,bargain_hunter_dict_of_products,user_shopping_cart).bargain_hunter_currency_options(currency_chosen,user_shopping_cart,bargain_hunter_dict_of_products,type_of_currency) # This calls the method inside the BargainHunters subclass which converts the currency
                        print(person_details) # prints the persons details returned from the CustomerClass
                        print(person_details.get_mobile()) # prints the persons details that are private inside the get_mobile method in the CustomerClass
                        print(customer_bargain) # prints the details in BargainHunters subclass
                        i = 2 # sets i = 2 meaning that this represents BargainHunter customer
                        use_option1_first = 1
                    elif type_of_customer.startswith('n') or type_of_customer.startswith('N'): # This is executed if the user chooses Need Based customer
                        person_details = CustomerClass(f_name,s_name,your_country,mobile_number) # calls CustomerClass and sends variables to it
                        customer_need_based = NeedBased(f_name,s_name,your_country,mobile_number,type_of_customer,need_based_customers_dict_of_products,user_shopping_cart) # calls NeedBased and passes the variables to it
                        type_of_currency = NeedBased(f_name,s_name,your_country,mobile_number,type_of_customer,need_based_customers_dict_of_products,user_shopping_cart).need_based_currency_options(currency_chosen,user_shopping_cart,need_based_customers_dict_of_products,type_of_currency)  # Calls the method within the NeedBased subclass which converts the currency
                        print(person_details) # prints the persons details returned from the CustomerClass
                        print(person_details.get_mobile()) # prints the persons details that are private inside the get_mobile method in the CustomerClass
                        print(customer_need_based) # prints the details in NeedBased subclass
                        i = 3 # sets i = 3 meaning that it represents NeedBased Customer
                        use_option1_first = 1 # This means that option 1 cannot be used once it is used once
                    else: # if neither loyal or bargain or need based customer is chosen
                        print("You didn't choose either option. You are going to be returned back to the main menu: ") # prints error message
                        i = 0 # sets i = 0 so that all the questions can be asked again and so that the user can change the type of customer if they want. This is only possible in the creating of the customer phase.
                        use_option1_first = 0 # option 1 can be used because there was an error
                        menu_choice = 0 # return to menu

                menu_choice = 0
            elif menu_choice == 1 and use_option1_first == 1: # if the menu choice is 1 but the user already created their customer
                print("Customer is already created!!!\n") # error message
                menu_choice = 0 # back to menu

            if menu_choice != 1 and use_option1_first == 0: # if the option was not 1 but the user still hasn't created a customer
                print("You must choose option 1 first: \n") # error message
                menu_choice = 0 # back to menu
            
            elif menu_choice == 2 and use_option1_first == 1: # if user chose option 2 and they have done option 1
                if i == 1: # if the user is a loyal customer
                    shopping_cart_1 = ShoppingCart(loyal_customers_dict_of_product,user_shopping_cart) # call the ShoppingCart class and pass both the list of products and the user shopping cart
                    print(shopping_cart_1) # print the list of products available for loyal customers
                    menu_choice = 0 # back to menu
                elif i == 2: # if the user is a bargain hunter
                    shopping_cart_1 = ShoppingCart(bargain_hunter_dict_of_products,user_shopping_cart) # calls the ShoppingCart class and passes both the list of products and the user shopping cart
                    print(shopping_cart_1) # print the list of products that are available for bargain hunters
                    menu_choice = 0 # back to menu
                elif i == 3: # if the user is a needs based customer
                    shopping_cart_1 = ShoppingCart(need_based_customers_dict_of_products,user_shopping_cart) # calls the ShoppingCart class and passes both the list of products and the user shopping cart
                    print(shopping_cart_1) # prints products available for needs based customers
                    menu_choice = 0 # back to menu
            elif menu_choice == 3 and use_option1_first == 1: # if the user chose option 3 and they already did option 1
                user_response = input("Do you want to add or remove a product?.If you want to add, type a. If you want to remove, type r: ") # asks if user wants to add or remove a product from their shopping cart
            
                if user_response.startswith('a') or  user_response.startswith('A'): # if the user wants to add, do this
                    if i == 1: # if they are a loyal customer
                        try: # try and look for an item number that is an integer
                            item_number = int(input("Which item number do you want to add to your shopping cart?"))
                        except ValueError: # expect that the user may enter a non-integer
                            print("You must choose an integer value as your item number") # print error message
                            menu_choice = 0 # back to menu
                        else: # if everything goes well
                            ShoppingCart(loyal_customers_dict_of_product,user_shopping_cart).adding_products(item_number) # call the adding_products method in ShoppingCart class
                            menu_choice = 0 # back to menu
                    elif i == 2: # if they are a bargain hunter
                        try: # try and look for an item number that is an integer
                            item_number = int(input("Which item number do you want to add to your shopping cart?"))
                        except ValueError: # expect that the user may enter a non-integer
                            print("Item number entered is not an integer. Try again") # print error message
                            menu_choice = 0 # back to menu
                        else: # if the user chose an integer
                            ShoppingCart(bargain_hunter_dict_of_products,user_shopping_cart).adding_products(item_number) # call the method adding_products in the ShoppingCart class
                            menu_choice = 0 # back to menu
                    elif i == 3: # if they are a needs based customer
                        try: # try and look for an item number that is an integer
                            item_number = int(input("Which item number do you want to add to your shopping cart?"))
                        except ValueError: # expect that the user may enter a non-integer
                            print("Number that you chose for the item is not an integer. Try again: ") # print error message
                            menu_choice = 0 # back to main menu
                        else: # if everything goes fine
                            ShoppingCart(need_based_customers_dict_of_products,user_shopping_cart).adding_products(item_number) # call method to add products 
                            menu_choice = 0 # back to menu
                elif user_response.startswith('r') or  user_response.startswith('R'): # if the user wants to remove a product, do this
                    if i == 1: # if they are a loyal customer
                        try: # try and look for an item number that is an integer
                            item_number = int(input("Enter the item number you wish to remove from the shopping cart: "))
                        except ValueError: # expect that the user may enter a non-integer
                            print("The item number you wish to remove is not an integer. Try again") # print error message
                            menu_choice = 0 # back to menu
                        else: # everything goes as it should
                            ShoppingCart(loyal_customers_dict_of_product,user_shopping_cart).removing_products(item_number) # call method removing_products from ShoppingCart class
                            menu_choice = 0 # back to menu

                    elif i == 2: # if they are a bargain hunter
                        try: # try and look for an item number that is an integer
                            item_number = int(input("Enter the item number you wish to remove from the shopping cart: "))
                        except ValueError: # expect that the user may enter a non-integer
                            print("Item number that you inputted is not an integer. Pick an integer, please") # print error message
                            menu_choice = 0 # back to main menu
                        else: # everything goes as it should
                            ShoppingCart(bargain_hunter_dict_of_products,user_shopping_cart).removing_products(item_number) # call method removing_products in ShoppingCart class
                            menu_choice = 0 # back to main menu
                    elif i == 3: # if they are a needs based customer
                        try: # try and look for an item number that is an integer
                            item_number = int(input("Enter the item number you wish to remove from the shopping cart: "))
                        except ValueError: # expect that the user may enter a non-integer
                            print("Item number that you inputted is not an integer. Choose an integer, please") # print error message
                            menu_choice = 0 # back to main menu
                        else: # if everything goes as expected
                            ShoppingCart(need_based_customers_dict_of_products,user_shopping_cart).removing_products(item_number) # call method removing_products in ShoppingCart class
                            menu_choice = 0 # back to the main menu
                else: # if neither add or remove product is entered
                    print("You must either choose to add or remove a product: ") # message printed
                    menu_choice = 0 # back to menu
            elif menu_choice == 4 and use_option1_first == 1: # if option 4 is selected and option 1 was already completed
                if i == 1: # if loyal customer
                    show_shopping_cart = ShoppingCart(loyal_customers_dict_of_product,user_shopping_cart).display_shopping_cart() # call the method display_shopping_cart in ShoppingCart class
                    print(show_shopping_cart) # print the user's shopping cart
                    menu_choice = 0 # back to menu
                elif i == 2: # if bargain hunter
                    show_shopping_cart = ShoppingCart(bargain_hunter_dict_of_products,user_shopping_cart).display_shopping_cart() # call the method display_shopping_cart in ShoppingCart class
                    print(show_shopping_cart) # print the user's shopping cart
                    menu_choice = 0 # back to menu
                elif i == 3: # if needs based customer
                    show_shopping_cart = ShoppingCart(need_based_customers_dict_of_products,user_shopping_cart).display_shopping_cart() # call the method display_shopping_cart in ShoppingCart class
                    print(show_shopping_cart) # print the user's shopping cart
                    menu_choice = 0 # back to menu
            elif menu_choice == 5 and use_option1_first == 1: # if user picked option 5 and they already finished option 1
                if i == 1: # if loyal customer
                    user_answer = ShoppingCart(loyal_customers_dict_of_product,user_shopping_cart).perform_checkout(type_of_currency)
                    if user_answer == 0: # if the user wants to continue shopping
                        menu_choice = 0 # back to menu
                elif i == 2: # if bargain hunter
                    user_answer = ShoppingCart(bargain_hunter_dict_of_products,user_shopping_cart).perform_checkout(type_of_currency)
                    if user_answer == 0: # if the user wants to continue shopping
                        menu_choice = 0 # back to menu
                elif i == 3: # if needs based customer
                    user_answer = ShoppingCart(need_based_customers_dict_of_products,user_shopping_cart).perform_checkout(type_of_currency)
                    if user_answer == 0: # if the user wants to continue shopping
                        menu_choice = 0 # back to menu

menu()
