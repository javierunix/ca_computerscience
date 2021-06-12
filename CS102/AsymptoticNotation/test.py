random_list = [4, 1, 8, 3, 0, 5, 9]

# sort the list
def sort_list(my_list):
	sorted_list = [] # empty list where we are going to store the sorted values
	mininum_value = my_list[0]
	while len(my_list) > 0:
		print(my_list)
	
		for item in my_list:
			if item <= mininum_value:
				mininum_value = item
		my_list.remove(mininum_value)

	return sorted_list

print(sort_list(random_list))