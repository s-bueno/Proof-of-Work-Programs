'''
This program assigns a random integer to the total rainfall for 12 months prior to the current date.
'''
# Import datetime module
import datetime
# Import random module
import random
# Creates a class with 4 parameters.
class Rainfall:
    # Instantiates the the class.
    def __init__(self, month, year, rain):
        self.month = month
        self.year = year
        self.rain = rain
    # Prints a string composed of the parameters given to the class.
    def myfunc(self):
        print(self.month+"("+self.year+")","=", self.rain)
# Creates an x variable and assigns a 0 value.    
x = 0
# Creates an total_rain variable and assigns a 0 value.
total_rain = 0
# Creates an empty list.
total_months = []
# Iterates over items in a given range.
for i in range(1,13):
    x += 30
    # Creates a variable delta and assigns the value from a datetime object.
    delta = datetime.timedelta(days=x)
    # Creates a variable now and assigns the current date.
    now = datetime.datetime.now()
    # Creates a months variable and assigns the a datetime object formatted to display only the month.
    month = (now - delta).strftime('%B')
    # Creates a year variable and assigns the a datetime object formatted to display only the year.
    year = (now - delta).strftime('%Y')
    # Creates a variable from a random integer in a given range.
    rain = random.randint(0,4)
    total_rain += rain
    # Creates a variable p1 and assigns the Rainfall object to it.
    p1 = Rainfall(month,year,rain)
    #Appends the p1 object to the total_months list.
    total_months.append(p1)
# Iterates over the items in total_months list.    
for i in total_months:
      # Calls the class method myfunc() for every item.
      i.myfunc()

print("-"*35)
# Prints total rain formatted to the second decimal.
print('Total rainfall:',('{:.2f}'.format(total_rain)))
# Prints average rain formatted to the second decimal.
print('Average rainfall:',("{:.2f}".format(total_rain/12)))