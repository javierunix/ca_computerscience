class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None

  def insert(self, value):
    if (value < self.value):
      if (self.left is None):
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        self.left.insert(value)
    else:
      if (self.right is None):
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)
        
  # Define .get_node_by_value() below:
  def get_node_by_value(self, value): 

    if self.value == value: # if the value of the node is equal to the target return the node
      return self
      
    elif self.left and value < self.value: # else if the target is lower and there is a left child, call the function on this child
      return self.left.get_node_by_value(value)

    elif self.right and value > self.value: # else if the target is higher and there is a right child, call the function on this child
      return self.right.get_node_by_value(value)

    else: # if the value is not found, return None
      return None
  
  
root = BinarySearchTree(100)

root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

# Get nodes by value below:
print(root.get_node_by_value(75).value)
print(root.get_node_by_value(55))
