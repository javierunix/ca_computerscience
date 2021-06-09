# 1 . *********************** recursive implementation of the factorial function **************************************
# runtime: Linear - O(N)

def factorial_recursive(n):
  global counter
  counter += 1
  if n < 0:    
    return ValueError("Inputs 0 or greater only") 
  elif n <= 1:    
    return 1  
  return n * factorial(n - 1)


# 2. *********************** iterative implementation of the factorial function **************************************
# runtime: Linear - O(N)

def factorial_iterative(n):
  result = 1
  if n < 0:    
    return ValueError("Inputs 0 or greater only") 
  elif n == 0:
    return result
  for i in range(1, n+1):
    result *= i
  return result

# 3. *********************** recursive implementation of the fibonacci function **************************************
# runtime: Linear - O(2^N)

def fibonacci_recursive(n):
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# 4. *********************** iterative implementation of the fibonacci function **************************************
# runtime: Linear - O(N)

def fibonacci_iterative(n):
  n_1 = 1
  n_2 = 0

  if n <= 1:
    result = n

  for i in range(2, n+1):
    result = n_1 + n_2
    n_2 = n_1
    n_1 = result

  return result

# 5. *********************** iterative implementation of the sum digits function **************************************

# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n != 0:
    result += n % 10
    n = n // 10
  return result + n
 
# print(sum_digits(12))
# # 1 + 2
# # 3
# print(sum_digits(552))
# # 5 + 5 + 2
# # 12
# print(sum_digits(123456789))
# # 1 + 2 + 3 + 4...
# # 45

# 5. *********************** recursive implementation of the sum digits function **************************************

def sum_digits_recursion(n):
  
  if n <= 9: # Base case: if n is a number with a unique digit
    return n
  last_digit = n % 10
  
  result = sum_digits_recursion(n // 10) + last_digit # recursive function
  
  return result

# print(sum_digits_recursion(12))
# print(sum_digits_recursion(552))
# print(sum_digits_recursion(123456789))

# 6. *********************** iterative implementation of the minimum function **************************************

def find_min(my_list):
  min = None

  for element in my_list:
    if not min or (element < min):
      min = element

  return min

find_min([42, 17, 2, -1, 67])
# -1
#find_mind([])
# None
find_min([13, 72, 19, 5, 86])
# 5

# 7. *********************** recursive implementation of the minimum function **************************************


def find_min(my_list, my_min = None):
  if not my_list:
    return my_min

  if not my_min or my_list[0] < my_min:
    my_min = my_list[0]
  return find_min(my_list[1:], my_min)

# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)


