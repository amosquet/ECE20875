from typing import List, Tuple

def histogram(input_dictionary: dict) -> list:
    # data is a dictionary that contains the following keys: 'data', 'n', 'min_val', 'max_val'
    # n is an integer
    # min_val and max_val are floats
    # data is a list

    # Write your code here

    # return the variable storing the histogram
    # Output should be a list

    #open dictionary and check if n is a positive integer, if not return empty list for 'hist
    if input_dictionary['n'] <= 0:
        return []
    
    #check if min_val and max_val are the same value, if so return empty list for 'hist'
    if input_dictionary['min_val'] == input_dictionary['max_val']:

        print('Error: min_val and max_val are the same value')
        return []
    
    #swap min_val and max_val if min_val is greater than max_val
    if input_dictionary['min_val'] > input_dictionary['max_val']:  
        input_dictionary['min_val'], input_dictionary['max_val'] = input_dictionary['max_val'], input_dictionary['min_val']
    
    hist = [0] * input_dictionary['n'] #initialize the histogram 'hist' as a list of n zeros
    w = (input_dictionary['max_val'] - input_dictionary['min_val']) / input_dictionary['n'] #calculate bin width

    #iterate through the data and increment the bin
    for val in input_dictionary['data']:

        if input_dictionary['min_val'] < val < input_dictionary['max_val']: #check if the value is within the range of the histogram

            bin = int((val - input_dictionary['min_val']) / w) #calculate the bin index
          
            hist[bin] += 1 #increment the bin

    return hist

# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def combine_birthday_data(person_to_day: List[Tuple[str, int]], 
                          person_to_month: List[Tuple[str, int]], 
                          person_to_year: List[Tuple[str, int]]) -> dict:
    #person_to_day, person_to_month, person_to_year are list of tuples

    # Write your code here

    # return the variable storing output
    # Output should be a dictionary

    month_to_people_data = {} #create empty dictionary
    current_year = 2024 #set current year

    #iterate over the person_to_month list
    for person, month in person_to_month:

        #extract day, year and age values from the person_to_day and person_to_year lists
        day, year, age = [day for name, day in person_to_day if name == person][0], [year for name, year in person_to_year if name == person][0], current_year - [year for name, year in person_to_year if name == person][0]
        if month in month_to_people_data: #check if month is already a key in the dictionary

            if isinstance(month_to_people_data[month], list): #check if the value is a list

                month_to_people_data[month].append((person, day, year, age)) #append the tuple to the list
            else:
                month_to_people_data[month] = [month_to_people_data[month], (person, day, year, age)] #change the value to a list and append the tuple
        else:
            month_to_people_data[month] = (person, day, year, age)

    return month_to_people_data


# We first define the current year as 2024, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_people_data that will store the final data in the format specified in the problem statement.
# We iterate over the both values in the tuple of the person_to_month list (note that person_to_month is a list of tuples, which means each item in the list is a tuple) 
# using a for loop. For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year lists using the current name as the "key".
# We then use the current month as the key and a tuple of (name, day, year, age) as the value to update the month_to_people_data dictionary.
# Only change the value to a list data type, when there are multiple entries with the same key. This will help append for other tuples to the same month.
# Finally, we return the month_to_people_data dictionary as the output of the function.
