'''
    This program calculates the ending principal in a bank account after compounding the interest.
'''
present_value = int(input("Enter the starting principal: $")) # Creates a variable named present_value from user input and converts it to an integer.
interest_rate = int(input("Enter the annual interest rate: ")) # Creates a variable named interest_rate from user input and converts it to an integer.
interest_frequency = int(input("How many times per year is the interest compounded? ")) # Creates a variable named interest_frequency from user input and converts it to an integer.
years = int(input("For how many years will the account earn interest? ")) # Creates a variable named years from user input and converts it to an integer.

# The following line creates a variable named future_value with a value derived from the equation for compound interest, rounded to the second decimal point, and then formatted to include commas when printed.
future_value = "{:,}".format(round(present_value * (1 + ((interest_rate/100)/interest_frequency))** (years * interest_frequency), 2)) 

print ("At the end of", years, "years you will have $", future_value) # Prints the account balance after the given amount of years.
