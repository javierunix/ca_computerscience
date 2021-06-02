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
  
    def remove_node(self, value_to_remove): 
        current_node = self.head_node

        if current_node.get_value() == value_to_remove: # if the value to remove is the current node
            self.head_node = current_node.get_next_node() # set the following node as new head

        else:
            while current_node:
                next_node = current_node.get_next_node() # find the following node
                if next_node.get_value() == value_to_remove: # if the following node is the node to remove
                    current_node.set_next_node(next_node.get_next_node()) # set the of the link of the current node to the node after the next node
                    break
                else:
                    current_node = next_node # in other case, set the next node as the new current.

    def swap_nodes(input_list, value1, value2):
        node1 = input_list.head_node
        node2 = input_list.head_node
        node1_prev = None # set the previous node to None
        node2_prev = None 

        while node1 is not None:
            if node1.get_value() == value1:
                break 
            node1_prev = node1 # set the previous node to be the current one
            node1 = node1.get_next_node() # set the current node to be the next

        while node2 is not None:
            if node2.get_value() == value2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if node1_prev is None:
            input_list.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            input_list.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        # updating the nodes' next pointers
        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)

        # edge cases
        if (node1 is None or node2 is None):
            print("Swap not possible - one or more element is not in the list")
            return

        if value1 == value2:
            print("Elements are the same - no swap needed")

# Create a method that returns the nth last element of a singly linked list.
    def list_nth_last(linked_list, n):
        linked_list_as_list = []
        current_node = linked_list.head_node
        while current_node:
            linked_list_as_list.append(current_node)
            current_node = current_node.get_next_node()
        return linked_list_as_list[len(linked_list_as_list) - n]

ll = LinkedList(0)
for i in range(10):
    ll.insert_beginning(i)
print(ll.stringify_list())
print(ll.list_nth_last(1).get_value())