'''
This program assigns a random integer to the total rainfall for a calendar year and writes them to a file.
'''
# Import random module
import random 
#Import datetime module
import datetime

# Populates the yearly_rain dictionary.
def rainfall():
    print("Printing Dictionary")
    # Iterates over items in a given range.
    for monthinteger in range(1,13):
        # Creates variable from a date give by the datetime module and formats it to only include the month.
        month = datetime.datetime(2022,monthinteger,1).strftime("%B")
        # Creates a variable from a random integer in a given range.
        rain = random.randint(0,4)
        # Appends items to yearly_rain dictionary, using month as key and rain as value. 
        yearly_rain [month] = rain
    print(yearly_rain)
# Attributes the sum of all values in yearly_rain to the variable total_rain. 
# Sorts and categorizes month as lowest_rain and highest_rain based on value for each month.  
def results():
    # The sum of all values yearly_rain. 
    total_rain = sum([i for i in yearly_rain.values()])
    # Sorts all items in yearly_rain by value.
    x = sorted(yearly_rain.items(),key = lambda kv:kv[1])
    # Determines the smallest value in yearly_rain.
    min = (x[0][1])
    # Determines the greatest value in yearly_rain.
    max = (x[-1][1])
    # Filters the months of with values equal to the max variable.
    highest_rain = filter(lambda a: a[1] == max, x)
    # Filters the months of with values equal to the min variable.
    lowest_rain = filter(lambda a: a[1] == min, x)
    
    print("-"*35)
    # Prints total_rain to the second decimal.
    print('Total rainfall:',('{:.2f}'.format(total_rain)))
    # Prints total_rain divided by 12 to the second decimal.
    print('Average rainfall:',("{:.2f}".format(total_rain/12)))
    # Prints all items filtered in the lowest_rain variable.
    print('Lowest rainfall: |'+"| ".join([i[0]for i in lowest_rain])+"|")
    # Prints all items filtered in the highest_rain variable.
    print('Highest rainfall: |'+"| ".join([i[0]for i in highest_rain])+"|")
    print('-'*35)
# Writes items from the yearly_rain dictionary into a text file in random order.
def write_to_file():
    print("\nPrinting Random Items to randout.txt")
    # Creates the file object that items will be written into.
    addMonth = open("randout.txt", "w")
    # Iterates over items in a given range.
    for i in range(1,13):
        # Creates a variable, key, that takes a random key and value from the yearly_rain dictionary.
        key = random.choice(list(yearly_rain.items()))
        # Writes boths key and value to the randout.txt file.
        addMonth.writelines([key[0]," - ",str(key[1]),"\n"])
        # Prints the string written into randout.txt.
        print(key[0]," - ",str(key[1]))
        # Deletes the key item from the yearly_rain dictionary.
        yearly_rain.pop(key[0])
    # Closes the file.
        
    addMonth.close()  

# Empty Dictionary   
yearly_rain = {} 
# Calls the rainfall function.         
rainfall()
# Calls the results function.
results()
# Calls the write_to_file function.
write_to_file()    