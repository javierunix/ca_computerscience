import node

class Queue:

	def __init__(self, max_size = None):
		self.head = None 
		self.tail = None 
		self.max_size = max_size
		self.size = 0

	def peek(self): 
		if not self.is_empty():
			return self.head.get_value() # return the value of the stack's head
		else:
			return("Nothing to see here!")

	def get_size(self):
		return self.size

	def has_space(self):
		if not self.max_size:
			return True
		else:
			if self.max_size > self.size:
				return True
			else:
				return False

	def is_empty(self):
		if not self.size: # if queue is empty return true
			return True
		else: # otherwise return false
			return False

my_queue = Queue()
print(my_queue.peek())