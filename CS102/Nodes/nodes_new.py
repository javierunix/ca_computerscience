# Define your Node class below:

class Node:

    # __init__() should take two arguments: value and next_node
    def __init__(self, value, next_node=None) -> None:
        self.value = value
        self.next_node = next_node

    # define a getter method for value
    def get_value(self):
        return self.value
    
    # define a getter method for next_node
    def get_next_node(self):
        return self.next_node

    # define a setter method for value
    def set_next_node(self, next_node):
        self.next_node = next_node

# # create an instance of Node with a value of 44
# my_node = Node(44)
# print(my_node.get_value())

# Create and empty LinkedList class

class LinkedList:

    # instantiate a LinkedList with a head node, so .__init__() should take value as an argument. 
    def __init__(self, value=None) -> None:
        self.head_node = Node(value) 

    # define a get_head_node() method
    def get_head_node(self):
        return self.head_node

    # define an insert_beginning() method
    def insert_beginning(self, new_value):
        new_node = Node(new_value) # instiate a new_node
        new_node.set_next_node(self.head_node) #link the new_node to the existing head_node
        self.head_node = new_node # replace the head node
 
    def stringify_list(self): #this method should transver the the list, beggining in the head list and collect every value
        my_list = []
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                my_list.append(current_node.get_value())
                current_node = current_node.next_node
        return my_list
  
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

