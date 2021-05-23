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

# print(count_multi_char_x("mississippi", "iss"))
# print(count_multi_char_x("apple", "pp"))

# ********************** 4 *****************************

# Write a function named substring_between_letters that takes a string named word, 
# a single character named start, and another character named end. 
# This function should return the substring between the first occurrence of start and end in word. 
# If start or end are not in word, the function should return word.

def substring_between_letters(word, start, end):
	
	start_position = word.find(start) # store in this variable the first ocurrence of start (-1 if not present)
	end_position = word.find(end) # store in this variable the first ocurrence of end (-1 if not present)

	if start_position == -1 or end_position == -1: # start or end character are not presente
		
		return word # return complete word
	
	return word[start_position+1:end_position] # otherwise, return substring between start and end

# print(substring_between_letters("apple", "p", "e"))
# print(substring_between_letters("apple", "p", "c"))


# ********************** 5 *****************************

# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. 
# This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
	
	words_list = sentence.split() # split the sentence into words, using blank spaces as break points

	for word in words_list: # loop over the list of words
		if len(word) < x:
			return False # if there is one word shorter than x return false

	return True # otherwise return true

print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))

