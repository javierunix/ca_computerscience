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