# We'll be using our Node class
class Node:

  def __init__(self, value, next_node=None):

    self.value = value
    self.next_node = next_node
    
  def get_value(self):

    return self.value
  
  def get_next_node(self):

    return self.next_node
  
  def set_next_node(self, next_node):

    self.next_node = next_node

# Our LinkedList class
class LinkedList:

  def __init__(self, value=None):

    self.head_node = Node(value)
  
  def get_head_node(self):

    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:
  def insert_beginning(self, new_value):

    self.new_node = Node(new_value)
    self.new_node.next_node = self.head_node
    self.head_node = self.new_node

  def stringify_list(self):

    node_list = []

    while True:

      node_list.append(self.head_node.value)

      if self.head_node.next_node == None:

        break

      else:  

        self.head_node = self.head_node.next_node

    return node_list

  def remove_node(self, value_to_remove):

      current_node = self.head_node

      if current_node.get_value() == value_to_remove:

        self.head_node = self.head_node.next_node

      else:

        while current_node:

          next_node = current_node.get_next_node()

          if next_node.get_value() == value_to_remove:

            current_node.set_next_node(next_node.get_next_node())
            current_node = None 

          else:
            current_node = next_node

# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)

ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)

print(ll.stringify_list())
