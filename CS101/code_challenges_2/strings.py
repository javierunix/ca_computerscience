# ********************** 1 *****************************

# Write a function called unique_english_letters that takes the string word as a parameter. 
# The function should return the total number of unique letters in the string. 
# Uppercase and lowercase letters should be counted as different letters.

def unique_english_letters(word):
	new_word = "" # create a new empty string
	for letter in word: # iterate over the word
		if letter not in new_word: # if the letter is not in the new string
			new_word += letter # add the letter to the new string
	return len(new_word) # return the length of the new string

# print(unique_english_letters("mississippi")) # should ouput 4
# print(unique_english_letters("Apple")) # should output 4

# ********************** 2 *****************************

# Write a function named count_char_x that takes a string named word and a single character named x as parameters. 
# The function should return the number of times x appears in word.

def count_char_x(word, x):
	counter = 0 # define and initialize counter
	for letter in word: # loop over the wword
		if letter == x: # if letter == parameter
			counter += 1 # increase counter
	return counter
# print(count_char_x("mississippi", "s"))
# print(count_char_x("mississippi", "m"))

# ********************** 3 *****************************

# Write a function named count_multi_char_x that takes a string named word and a string named x. 
# This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. 
# However, this time, make sure your function works when x is multiple characters long.

def count_multi_char_x(word, x):
	# the function split() create a list when the fragments created when the word is splitted using x as breakpoint
	return len(word.split(x)) - 1  # the number of break points is fragments minus 1

print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))