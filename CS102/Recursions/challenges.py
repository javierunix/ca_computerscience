# Define a function called move_to_end() that accepts two arguments: lst and val.

# The function should return a copy of lst with every instance of val moved to the end of the list.

# Example:

# Input: move_to_end(["Amber", "Sapphire", "Amber", "Jade"], “Amber”)
# Output: ["Sapphire", "Jade", "Amber", "Amber"]

lst = ["Amber", "Amber", "Sapphire", "Jade"]
val = "Amber"


def move_to_end(lst, val):
	
	result = [] # create new empty list to store the result

	if len(lst) == 0: # base case when the length of the list is 0 
		return []

	if lst[0] == val: # if the first element is equal to the val
		result += move_to_end(lst[1:], val) # iterate over the rest of the list
		result.append(lst[0]) # append the first element at the end of the list

	else:
		result.append(lst[0]) # append the first element at the beginning of the list
		result += move_to_end(lst[1:], val) # iterate over the rest of the list

	return result
 
# gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
# print(move_to_end(gemstones, "Amber"))

# **************** Prepend and append to a string ***************

# define a function that accepts two arguments a string and and integer
# the function should return a copy of the string with n copies of '<' and '>'

def wrap_string(my_string, my_integer):
	
	result = "" # create a result variable and assign to empty string
	
	# print("breakpoint 1")
	# print("String: %s\tInteger: %d" %(result, my_integer))
	
	if my_integer <= 0:
		return my_string
	result += "<" + wrap_string(my_string, my_integer - 1) + ">"
	
	# print("breakpoint 2")
	# print("String: %s\tInteger: %d" %(result, my_integer))

	return result


wrapped = wrap_string("Pearl", 3)
print(wrapped)