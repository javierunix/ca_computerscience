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
 
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))