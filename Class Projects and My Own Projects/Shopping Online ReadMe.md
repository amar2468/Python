************************************************************Shopping Online Documentation**************************************************

This document contains information on the project that I completed, which is called ShoppingOnline.py

A class called ShoppingCart which is based on the shopping cart in which the customer can see their shopping cart and they can add products or remove them from their shopping cart and they can perform a checkout where the total will be presented and necessary error-checking is done. 

In the __init__ method, the arguments that were received are used to initialise the variables. The specific dictionary of products available and the user shopping cart were the arguments given.

In the adding_products method, the keys from the dictionary of products available are put inside a list so that when the customer looks for a specific item number, it will look for the index and find the key needed e.g. if the user chooses item number 1, it will know that the first element in the list is 1. The reason why the item number is subtracted by 1 is because elements start from 0 and if the customer enters 1, I want the program to then take the element from 0 as 1. That way, the first element will be item number 1 and so on. Then, similar was done for values as was for keys. The .values() was used in order to show only the values and then this was put inside a list so that it can be accessed via the item number chosen by the customer. Finally, the key:value needed was put inside the customer’s shopping cart.  
As for the method regarding removing products, the dict of products keys are put inside a list. Then, using the item number as explained above, the key can be removed from the customer shopping cart using pop(). 

The next method in this class is display_shopping_cart and it basically shows the customer’s shopping cart which is needed in option 4 of the menu. 
Then, the method perform_checkout is used. If the customer shopping cart is empty, an error message is shown. Using the variable continue_shopping, the customer is redirected back to the main menu. If the customer shopping cart is not empty, then a for loop is used and it iterates through the values inside the shopping cart of the customer and adds the price to the current total. The total is printed out along with the currency that the user picked in the menu. If the user is happy with everything, a message is printed and the program exits. If they want to continue shopping, they are redirected back to the main menu. In the case that they did not correctly select yes or no, they are returned back to the main menu. 

Finally, the __str__ method returns the products available for purchase depending on whether you are a loyal customer, bargain hunter or needs based customer. 
The next class that was created was CustomerClass. This class represents the customer information such as their personal details and the type of customer that they are. The latter is put into three subclasses. 

The __init__ method takes the arguments and initialises them inside the constructor. Then, there are set_mobile and get_mobile methods. The set_mobile initialises the variable with the mobile number and then get_mobile returns the mobile number. 

The __str__ methods prints the customer personal details.

There are three subclasses that inherit attributes from CustomerClass. They are: LoyalCustomers, BargainHunters and NeedBased. All of these subclasses are similar to each other.
The LoyalCustomers consists of an __init__ method that initialises the variables and inherits the attributes from CustomerClass. This means that inheritance is the relationship between the subclass and the CustomerClass. 

The currency_conversions method receives arguments such as loyal customer dictionary of products and the currency. If the customer chooses euro, the euro will be printed when the customer performs a checkout. If they choose dollars, there is a for loop that iterates over the key,value of the loyal customer dict of products and multiplies the price by the exchange rate. This creates a new price that will be displayed if user enters option 2. 

Finally, the __str__ method prints what type of customer you are, which in this case is a loyal customer. 

The same process was done with BargainHunters. The __init__ initialises the variables and then inherits attributes from CustomerClass.
The bargain_hunter_currency_options method converts the prices to dollars or keeps them as euros. If the customer chooses euros, the euro will be used. If they pick dollars, there is a for loop that iterates over the key,value of the bargain hunter dict of products and multiplies the price by the exchange rate. This creates a new price that will be displayed if user enters option 2. 

At the end, the __str__ method returns the customer type which is a bargain hunter.
NeedBased was done the same way as the other two subclasses. The __init__ method initialised the variables and attributes were inherited from CustomerClass. 
The method need_based_currency_options converted the currency if needed using the same steps as the other two subclasses above. Finally, the __str__ returned the customer type which was a need based customer.

Now, the menu() will be explained. Three dictionary of products were created representing each of the types of customers available. One dictionary was also created representing the customer shopping cart where they can add or remove the products. A variable called use_option1_first guaranteed that once the customer was created, the user cannot do option 1 again. Variable menu_choice symbolised the menu option and the i variable is set to 0. The i variable is there so that one can call the class depending on what type of customer they are. If the user enters wrong info into option 1, there will be an error message and the user can do option 1 again because they entered invalid details. If no incorrect details are entered, the value of i will either be 1 or 2 or 3 depending on what customer type they are. 

In option 2, it can only be executed if the user has done option 1 successfully. Depending on what customer type they are, the subclass will be called and arguments such as the dictionary of products of that customer type and the customer’s shopping cart will be passed. 

In option 3, the customer is asked whether they want to add/remove a product. If they want to add, a try/except block is created and they are asked what item number they want to add. If they want to add the first item from the list, they enter 1 and so on. Then, the method is called that performs the adding of products. It is important to note that the item number must be an integer in order for this to work. Again, the dictionary of products will depend on the customer type that the customer chose in option 1. 
In option 4, the ShoppingCart class has the method called display_shopping_cart which is called and the customer shopping cart is presented on screen. 
Finally, option 5 performs checkout by calling the method perform_checkout which is inside the ShoppingCart class. If the method returns the value 0, then the user continues shopping. This depends on whether the user wants to continue to shop or if they are happy with the products.

The user manual for this system is as follows. When the customer chooses option 1, they type in their name, surname, country, mobile number, currency of choice and the type of customer they are. The customer is created. Then, option 2 shows the dictionary of products depending on what customer they are. Then, option 3 allows the customer to add or remove products from their shopping cart. Option 4 shows them their shopping cart with added/removed items. Option 5 shows the total price along with the currency and asks the user whether they want to continue shopping or not. If the user does not want to continue, a message is printed to screen and they exit out of the shop. Otherwise, they are returned back to the main menu. 

If you wish to run this program, it is very simple. First, install an IDE and the compiler for Python. Then, use the source code from ShoppingOnline.py. Once you run the program,follow the steps given in the user manual.

