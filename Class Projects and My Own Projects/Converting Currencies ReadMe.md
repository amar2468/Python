************************************************Converting Currencies************************************************


This is the documentation for the project called ConvertingCurrencies.py


This project is a simple one that uses API to take information that can be useful in the project. Firstly, I imported urllib.request so that I can open the website needed.

I also created a class called currency. Inside this class, I created a list that had the list of valid currencies. The currency class consists of many methods which will all be separately explained.

The __init__ method initialises the variables that are passed in. I made an if statement that checks whether the currency type is in the valid currencies list. If yes, initialise the self.amount and self.currency type. Otherwise, set the variable values to 0 and an empty string. 

The convert_to() method is responsible for converting the currencies. It first starts off with a simple check to see whether the new currency type is the same as the old one. If yes, it just returns the currency along with the amount because there is nothing else to do. If the new currency is not in the valid currencies, error message is printed and a return statement is used. Then, the url variable is created. This variables stores the API link to the currency conversion API. The currency type is concatenated to the url as well as the new currency type. Then, a dictionary is created and json library is used so that you can load the response into the dictionary. The exchange amount variable is used to store the rate of the new currency type. Then, this is multiplied by the amount. Finally, this is returned back. 

The __str__ function prints out the amount for the currency type.

Note: This project will be further improved. I am making many changes to it. Expect many changes in the coming weeks.
