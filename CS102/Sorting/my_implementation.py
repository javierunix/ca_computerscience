def binary_search(my_list, target_value, count = 0):
    
    count += 1 # variable to count the number of iterations
    # define base case when the target list contains a single element
    if len(my_list) <= 1: 
        return my_list[0], count # return the element of the list and the counter variable

    # define the index to divide the list
    middle_index = len(my_list) // 2 

    # create two sublist by dividing the previous one in the middle index
    left_half = my_list[:middle_index] 
    right_half = my_list[middle_index:]

    # if target is greater than the last element of the left sublist, the target must be in the right sublist
    if target_value > left_half[-1]: 
        return(binary_search(right_half, target_value, count)) # recursive call in the right half of the list
    
    # if target is eaqual or lower than the last element of the left sublist, the target must be in the left sublist
    else:
        return(binary_search(left_half, target_value, count)) # recursive call in the left half of the list
    


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target_value = 4

print(binary_search(my_list, target_value))