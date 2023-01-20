'''
    This program print a W pattern when conditions are met.
'''

character = '*' # The symbol to print 
space = ' '     # The space character 

# Number of rows from user input
numRows = int(input('Enter the number of rows between 7 and 10: '))

# Range of numbers used in loop
if numRows in range(7,11):
    
    # Print line
    print('\n')
    
    # Iterate over the rows in revesed order. 
    for row in reversed(range(numRows)): 
        
        # Each row includes the number of rows plus 2 more columns 
        # than the row number. 
        for col in range((numRows+numRows) + 2): 
            
            # Print the symbol in the first and last column.
            # Print symbol in inverted V pattern
            if col == 0 or col == row + 1 or col == ((numRows+numRows)) or col == ((numRows+numRows)) - (row+1): 
                print(character, end='') 
                
            # Add spaces between symbols. 
            else:   
                print (space, end='') 
    
        # Go to the next row. 
        print() 

# Print statement        
else:
    print("--- Incorrect entry. Please try again.---")