class Node:

	def __init__(self, value, next_node = None, prev_node = None):
		self.value = value
		self.next_node = next_node
		self.prev_node = prev_node

	def set_next_node(self, next_node):
		self.next_node = next_node

	def get_next_node(self):
		return self.next_node

	def set_prev_node(self, prev_node):
		self.prev_node = prev_node

	def get_prev_node(self):
		return self.prev_node

	def get_value(self):
		return self.value

class DoublyLinkedList:

	def __init__(self): # only self as parameter since the list will be created empty
			self.head_node = None 
			self.tail_node = None

	def add_to_head(self, new_value):
		new_head = Node(new_value)
		current_head = self.head_node

		if current_head is not None: # if there is a current head 
			current_head.set_prev_node(new_head) # set the new_head the previous node of current head
			new_head.set_next_node(current_head) # set the current head to be the next node of the new head

		self.head_node = new_head # set the list head to the new_head

		if self.tail_node is None: # if the list does not have a tail
			self.tail_node = new_head # set the new_head to be the tail node 


	def add_to_tail(self, new_value):
		new_tail = Node(new_value)
		current_tail = self.tail_node

		if current_tail is not None:
			current_tail.set_next_node(new_tail)
			new_tail.set_prev_node(current_tail)

		self.tail_node = new_tail

		if self.head_node is None:
			self.head_node = new_tail

	def remove_head(self):
		removed_head = self.head_node # set the removed head to the current head

		if removed_head is None:
			return None 

		self.head_node = removed_head.get_next_node() # set the next node as head
			
		if self.head_node is not None:
			self.head_node.set_prev_node(None) # set the previous node to be None

		if removed_head == self.tail_node: # if the head is the tail, call the method remove_tail()
			self.remove_tail()

		return removed_head.get_value() # return the value of removed_head

	def remove_tail(self):
		removed_tail = self.tail_node

		if removed_tail is None:
			return None 

		self.tail_node = removed_tail.get_prev_node()

		if self.tail_node is not None:
			self.tail_node.set_next_node(None)

		if removed_tail == self.head_node:
			self.removed_tail()

		return removed_tail.get_value()

	def remove_by_value(self, value_to_remove):
		node_to_remove = None
		current_node = self.head_node

		while current_node is not None:
			if current_node.get_value() == value_to_remove:
				node_to_remove = current_node
				break
			current_node = current_node.get_next_node()

		if node_to_remove is None:
			return None 

		elif node_to_remove == self.head_node: # if node is head call the remove_head (method)
			self.removed_head()

		elif node_to_remove == self.tail_node: # if node is tail call the remove_tail (method)
			self.removed_tail()

		else: # if node is in the middle, change the pointers of prev a next nodes
			next_node = node_to_remove.get_next_node()
			prev_node = node_to_remove.get_prev_node()

			prev_node.set_next_node(next_node) 
			next_node.set_prev_node(prev_node)

		return node_to_remove

	def stringify_list(self): 
		my_list = []
		current_node = self.head_node

		while current_node:
			if current_node.get_value() != None:
				my_list.append(current_node.get_value())
				current_node = current_node.next_node
		return my_list


subway = DoublyLinkedList()

subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")

# delete "Central Park" and "Brooklyn Bridge" without iterating through the list
subway.remove_head() 
subway.remove_tail()

subway.remove_by_value("Times Square")


print(subway.stringify_list())


