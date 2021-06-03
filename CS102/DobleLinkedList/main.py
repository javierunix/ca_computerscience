class Node:

	def __init__(self, value, next_node = None, prev_node = None):
		self.value = value
		self.next_node = next_node
		self.prev_node = prev_node

	def set_next_node(self, next_node):
		self.next_node = next_node

	def get_next_node(self):
		return next_node

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

