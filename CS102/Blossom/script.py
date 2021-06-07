from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
				
	def __init__(self, size):	#Give HashMap a constructor that takes a size parameter. 
		self.array_size = size # Save size into self.array_size.					
		self.array = [LinkedList() for i in range(self.array_size)] #Create a list of None objects of length size and save it into self.array.

	def hash(self, key):
		key_bytes = key.encode()
		hash_code = sum(key_bytes)
		return hash_code

	def compress(self, hash_code):
		return hash_code % self.array_size

	def assign(self, key, value):
		array_index = self.compress(self.hash(key))
		payload = Node([key, value])
		
		list_at_array = self.array[array_index]

		for every_item in list_at_array:
			if every_item[0] == key:
				every_item[1] = value
				return

		list_at_array.insert(payload)


	def retrieve(self, key):
		array_index = self.compress(self.hash(key))
		list_at_index = self.array[array_index]

		for every_item in list_at_index:
			if every_item[0] == key:
				return every_item[1]

		return None

blossom = HashMap(len(flower_definitions))

for every_item in flower_definitions:
	blossom.assign(every_item[0], every_item[1])

print(blossom.retrieve('hyacinth'))