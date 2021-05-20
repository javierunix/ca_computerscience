# 1. Create a function named larger_sum() that takes two lists of numbers 
# as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number.
#  If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    return max(sum(lst1), sum(lst2)) # return the max sum list

# print(larger_sum([1, 9, 5], [2, 3, 7]))

# 2. Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater than 9000. 
# When this happens, the function should return the sum. 
# If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. 
# If the list is empty, the function should return 0.
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

def over_nine_thousand(lst):
    sum = 0 # initialize sum
    i = 0 # initialize counter
    while sum <= 9000: # while the sum is not greater than 9000
        sum += lst[i]  # add new element to sum
        i += 1 # increase counter
    return sum 
# print(over_nine_thousand([8000, 900, 120, 5000]))

# 3. Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums

def max_num(nums):
    maximus = nums[0] # set the first number of the list as default maximus
    for i in range(1, len(nums)): # iterate over the list
        if nums[i] > maximus: # if current element is greater than current maximus
            maximus = nums[i] # current element is the new maximus
    return maximus
print(max_num([50, -10, 0, 75, 20]))    

