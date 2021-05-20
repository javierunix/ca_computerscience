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
    my_list = lst # copy in a new list the argument, in order to avoid conflict between local and global variables
    i = 0 # create index counter
    while i < len(my_list): # iterate over list
        if my_list[i] % 2 == 0: # if the element is even
            my_list = my_list[i+1:] # the list is shorten 
        else:
            break  #get out the loop once the first even element has been found
    return(my_list)
            
        
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10, 14, 18, 20]))