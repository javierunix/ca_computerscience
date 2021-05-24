# ********************** 1 *****************************

# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. 
# The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
	return sum(my_dictionary.values()) # 

# print(sum_values({10:1, 100:2, 1000:3}))
# print(sum_values({"milk":5, "eggs":2, "flour": 3}))


# ********************** 2 *****************************

# Create a function called sum_even_keys that takes a dictionary named my_dictionary, 
# with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.

def sum_even_keys(my_dictionary):
	sum = 0
	for i in my_dictionary.keys(): # iterate over keys
		if i % 2 == 0: # key is even
			sum += my_dictionary[i] # add value to sum
	return sum
# print(sum_even_keys({1:5, 2:2, 3:3}))
# print(sum_even_keys({10:1, 100:2, 1000:3}))


# ********************** 3 *****************************

# Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
# The function should add 10 to every value in my_dictionary and return my_dictionary

def add_ten(my_dictionary):

	for key in my_dictionary.keys():
		my_dictionary[key] += 10 # increment value in 10

	return my_dictionary

# print(add_ten({1:5, 2:2, 3:3}))
# print(add_ten({10:1, 100:2, 1000:3}))

# ********************** 4 *****************************

# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
# This function should return a list of all values in the dictionary that are also keys.

def values_that_are_keys(my_dictionary):

	my_list = []
	for value in my_dictionary.values(): # iterate over values
		if value in my_dictionary: # return true if value is also a key
			my_list.append(value)
	return my_list

# print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))

# ********************** 5 *****************************

# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
# The function should return the key associated with the largest value in the dictionary.

def max_key(my_dictionary):

	max_value = float('-inf') #Initialize the starting value to a very low number
	max_key = float('-inf') #Initialize the starting key to a very low number

	for key, value in my_dictionary.items():

		if value > max_value:
			max_value = value
			max_key = key

	return max_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))



