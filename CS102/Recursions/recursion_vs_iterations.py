# recursive implementation of the factorial function
# runtime: Linear - O(N)
def factorial(n):
  global counter
  counter += 1
  if n < 0:    
    return ValueError("Inputs 0 or greater only") 
  elif n <= 1:    
    return 1  
  return n * factorial(n - 1)

counter = 0
print(factorial(3))
print(counter)

counter = 0
print(factorial(4))
print(counter)

counter = 0
print(factorial(0))
print(counter)

# 1
print(factorial(-1))
# ValueError "Input must be 0 or greater"