# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
    counter = 0 # define and initialize counter
    for num in nums: # iterate over list
        if num % 10 == 0: # if number is divisible by ten
            counter += 1 # increment counter
    return counter
# print(divisible_by_ten([20, 25, 30, 35, 40]))

# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.

def add_greetings(names):
    greetings = []
    for name in names:
        greetings.append("Hello, %s" %name)
    return greetings
    
# print(add_greetings(["Owen", "Max", "Sophie"]))

#Write a function called delete_starting_evens() that has a parameter named lst.
# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return(lst)
            
        
# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# print(delete_starting_evens([4, 8, 10, 14, 18, 20]))


# Create a function named odd_indices() that has one parameter named lst.
# The function should create a new empty list and add every element from lst that has an odd index. 
# The function should then return this new list.

def odd_indices(lst):
    new_list = [] 
    for i in range(1, len(lst), 2): # iterate from index 1, in 2 position steps 
        new_list.append(lst[i])
    return new_list
# print(odd_indices([4, 3, 7, 10, 11, -2]))

# Create a function named exponents() that takes two lists as parameters named bases and powers. 
# Return a new list containing every number in bases raised to every number in powers.

def exponents(bases, powers): # the function accepts as arguments two lists: bases and powers
    new_list = [] # new list to store the exponents
    for base in bases: # iterate through bases
        for power in powers: # iterate through powers
            new_list.append(base ** power) # append to new list the exponential number
    return new_list
print(exponents([2, 3, 4], [1, 2, 3])
)
