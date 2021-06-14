nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp
  
# define bubble_sort():
def bubble_sort(arr):
  for el in arr:
    for index in range(len(arr)-1):
      if arr[index] > arr[index + 1]:
        swap(arr, index, index + 1)


##### test statements

print("Pre-Sort: {0}".format(nums))      
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))

def merge_sort(my_list):
  # when the list is length return the list
  if len(my_list) <= 1:
    return my_list

  middle_idx = len(my_list) // 2 # calculate the middle point of the list
  left_split = my_list[:middle_idx] # first half of the list
  right_split = my_list[middle_idx:] # second half of the list

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []
  while left and right:
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  if left:
    result += left
  elif right:
    result += right
  
  return result

print(merge_sort(nums))