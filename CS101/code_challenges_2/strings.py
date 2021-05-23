# Write a function called unique_english_letters that takes the string word as a parameter. 
# The function should return the total number of unique letters in the string. 
# Uppercase and lowercase letters should be counted as different letters.

def unique_english_letters(word):
	new_word = "" # create a new empty string
	for letter in word: # iterate over the word
		if letter not in new_word: # if the letter is not in the new string
			new_word += letter # add the letter to the new string
	return len(new_word) # return the length of the new string

print(unique_english_letters("mississippi")) # should ouput 4
print(unique_english_letters("Apple")) # should output 4