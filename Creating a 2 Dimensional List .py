'''
 This program assigns a random integer to the total rainfall for a calendar year.
'''
# Import random module
import random

# Populates a 2 Dimensional list and prints out said list.
def rainfall():
    # List containing months of the year. 
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    
    print('Printing 2 Dimensional list\n')
    # Iterates over items in months list
    for i in months:
        # Attributes a random value from given range to the variable rain.
        rain = random.randint(0,4)
        # Appends both the iterated item from months and the value of rain to the empty list titled empty.
        empty.append([i,rain])
    # Prints the "empty" list as a string.    
    print(empty,"\n")
    print('Month | Rainfall\n'+('-'*14))
    # Iterates over the items in "empty" list.
    for i in empty:
        # Print first and second index of itereated item.
        print(i[0],i[1])
    print('-'*35)

# Populates the range, high_rainfall, and low_rainfall lists.        
def min_max():
    # Iterates over the items in "empty" list.
    for i in empty:
        # Appends the second index of the iterated item to the "range" list.
        range.append(i[1])
    # Sorts the items in the values in the range list from lowest to highest.    
    range.sort()
    # Attributes the lowest value from range list to the variable min.
    min = range[0]
    # Attributes the highest value from range list to the variable max.
    max = range[-1]
    # Iterates over the items in "empty" list.
    for i in empty:
        # Sets parameters for appending item to list.
        if i[1] == max:
            # Appends the first index from the iterated item to the high_rainfall list.
            high_rainfall.append(i[0])
        # Sets parameters for appending item to list.    
        elif i[1] == min:
            # Appends the first index from the iterated item to the low_rainfall list.
            low_rainfall.append(i[0])

# Attributes the sum of all items in range to the variable total_rain.
# Prints total yearly rain, average yearly rain, Lowest rain month, and highest rain month.         
def results():
    # Attributes the sum of all items in range to the variable total_rain.
    total_rain = sum(range)
    # Prints total yearly rain formatted to the second decimal.
    print('Total rainfall:',('{:.2f}'.format(total_rain)))
    # prints average yearly rain formatted to the second decimal.
    print("Average rainfall:",("{:.2f}".format(total_rain/12)))
    # Prints the lowest rainfall months.
    print('Lowest rainfall:', ", ".join([i for i in low_rainfall]))
    # Prints the highest rainfall months
    print('Highest rainfall:', ", ".join([i for i in high_rainfall]))
    print('-'*35,'\n')

# Sorts the "empty" list by the second index and prints the list. 
def sorted_rainfall():
    # Sorts the "empty" list by the second index.
    empty.sort(key=lambda i:i[1])
    print('Months sorted by rainfall\n'+
          'Ordered by Calendar Month\n'+
          ('-'*35))
    # Iterates over the items in the sorted empty list.
    for i in empty:
        # Prints the first and second index of the iterated item.
        print(i[0],i[1])

# Empty list that are populated by the rainfall and min_max functions.
empty = []
range = []
low_rainfall = []
high_rainfall = []

# Calls the rainfall function.
rainfall()
# Calls the min_max function.
min_max()
# Calls the results function.
results()
# Calls the sorted_rainfall function.
sorted_rainfall()