class HashMap:

	def __init__(self, array_size):
		self.array_size = array_size 
		self.array = [None for i in range(self.array_size)] # list of size array_size


	def hash(self, key):
		key_bytes = key.encode() # turn the key into a list of bytes
		hash_code = sum(key_bytes) # turn the list of bytes into a hash
		return hash_code

	# create compressor function. it takes the modulus of hash_code by self.array_size
	def compressor(self, hash_code):
		return hash_code % self.array_size