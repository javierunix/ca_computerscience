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

# print(max_key({1:100, 2:1, 3:4, 4:10}))
# print(max_key({"a":100, "b":10, "c":1000}))

# ********************** 6 *****************************

# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
# The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

def word_length_dictionary(words):
	
	my_dict = {} # create and initialize dictionary
	for word in words:
		my_dict[word] = len(word) # add word as key and length of word as value

	return my_dict

# print(word_length_dictionary(["apple", "dog", "cat"]))
# print(word_length_dictionary(["a", ""]))

# ********************** 7 *****************************

# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. 
# The function should return a dictionary containing the frequency of each element in words.

def frequency_dictionary(words):
	
	my_dict = {} # create and initialize dictionary
	for word in words:
		if word not in my_dict:
			my_dict[word] = 0 # initialize as 0
		my_dict[word] += 1 #if word already in dict increment count by 1
	return my_dict

# print(frequency_dictionary(["apple", "apple", "cat", 1]))
# print(frequency_dictionary([0,0,0,0,0]))
# ********************** 8 *****************************

# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. 
# The function should return the number of unique values in the dictionary.

def unique_values(my_dictionary):
	unique_values = []

	for value in my_dictionary.values(): # loop over values
		if value not in unique_values: # if value not already in list
			unique_values.append(value) # append the value
	return len(unique_values)

# print(unique_values({0:3, 1:1, 4:1, 5:3}))
# print(unique_values({0:3, 1:3, 4:3, 5:3}))

# ********************** 9 *****************************

# Create a function named count_first_letter that takes a dictionary named names as a parameter. 
# names should be a dictionary where the key is a last name and the value is a list of first names.

def count_first_letter(names):

	my_dict = {}

	for key, value in names.items():
		first_letter = key[0]
		if first_letter not in my_dict:
			my_dict[first_letter] = 0
		my_dict[first_letter] += len(value)

	return my_dict

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
