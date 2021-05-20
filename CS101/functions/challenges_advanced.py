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

# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.
# For example, the following code should return [0, 2, 3]:
# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

def same_values(nums1, nums2):
    index_list = []
    for i in range(len(nums1)):
        if nums1[i] == nums2[i]:
            index_list.append(i)
    return index_list
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

def reversed_list(lst1, lst2):
    reversed = True # set this variable as true as default
    for i in range(len(lst1)):
        if lst1[i] != lst2[-( i+ 1)]: # if a element is different its symmetrical
            reversed = False # ... then the list are no reversed
    return reversed
print(reversed_list([1, 2, 3], [3, 2, 1]))