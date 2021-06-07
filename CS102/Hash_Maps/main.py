class HashMap:

	def __init__(self, array_size):

		self.array_size = array_size 
		self.array = [None for i in range(self.array_size)] # list of size array_size


	def hash(self, key, count_collisions = 0): # the function takes as paramenters the key and a counter of collisions

		key_bytes = key.encode() # turn the key into a list of bytes
		hash_code = sum(key_bytes) # turn the list of bytes into a hash
		return hash_code + count_collisions

	# create compressor function. it takes the modulus of hash_code by self.array_size
	def compressor(self, hash_code):

		return hash_code % self.array_size

	def assign(self, key, value):

		array_index = self.compressor(self.hash(key)) # the index is determined by plugin the key into the hash and the hash_code into the compressor
		current_array_value = self.array[array_index] # check the content currently in the index
		
		if current_array_value is None: # if there is not current value for this index
			self.array[array_index] = [key, value] # save the key and value
			return
		
		if current_array_value[0] == key: # if the key is the same, overwrite the value 
			self.array[array_index] = [key, value]
			return
		
		# when the key considered is different to the key in the hash code, we have to take into account the number of collisions
		number_collisions = 1

		while current_array_value[0] != key:
			new_hash_code = self.hash(key, number_collisions) # create a new hash code considering the number of collisions
			new_array_index = self.compressor(new_hash_code) # create a new index
			current_array_value = self.array[new_array_index]

			if current_array_value is None:
				self.array[new_array_index] = [key, value]
				return

			if current_array_value[0] == key:
				self.array[new_array_index] = [key, value]
				return

			number_collisions += 1


	def retrieve(self, key):

		array_index = self.compressor(self.hash(key))
		possible_return_value = self.array[array_index]

		if possible_return_value is None: # if there is no value for this key
			return None

		elif possible_return_value[0] == key: # if the key of the possible value is the same as the provided 
			return possible_return_value[1] # return the value

		retrieval_collisions = 1

		while (possible_return_value[0] != key):
			new_hash_code = self.hash(key, retrieval_collisions)
			retrieving_array_index = self.compressor(new_hash_code)
			possible_return_value = self.array[retrieving_array_index]

			if possible_return_value is None:
				return None
			
			if possible_return_value[0] == key:
				return possible_return_value[1]

			retrieval_collisions += 1
# test with one example 
hash_map = HashMap(15) # create a hash of size 15

hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")

print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))

