
# **************************** Data Types ****************************

# Python types refers to the way the python interpreter store the data.
# We can check the data type using the built-in type() function 

# 1. Call type(5) and print the result
# print(type(5))
# output: <class 'int'>

# 2. Define a dictionary and print the type
my_dict = {}
# print(type(my_dict))
# output = <class 'dict'>

# 3. Same for a list
my_list = []
# print(type(my_list))
# output = <class 'list'>

# **************************** Class ****************************

# A Class is a template for a data type. It describes the kinds of information that class
# will hold and how a programmer will interact with that data.

# 1. Create a class called Facade

class Facade():
	
	pass

# 2. Create an instance of the class

facade_1 = Facade()

# 3. Check the type facade_1

facade_1_type = type(facade_1)

# print(facade_1_type) 

# **************************** Class Variables ****************************


# 4. A class variable is the same for all the instances of a class
# Create a Grade class with a class attribute minimum_passing equal to 65.

class Grade():

	minimum_passing = 65

# **************************** Methods ****************************

# 5. Methods are functions that are defined as a part of a class.
# The first argument is always the object that is calling the method ('self' by convention)

class Rules():

	def washing_brushes(self): # defining method, passing the object as argument
		
		return("Point bristles towards the basin while washing your brushes.")

rule1 = Rules()
# print(rule1.washing_brushes())

# **************************** Methods with Arguments ****************************

# class Circle():
	
# 	pi = 3.14 # class variable

# 	def area(self, radius): # method than receive as parameters the object and its radius
# 		return self.pi * radius ** 2 # we pass self.pi because is a class variable

# circle = Circle() # create an instance of the class

# # calculate the area given 3 different diameters 
# pizza_area = circle.area(12 / 2) # diameter == 12 => radius = 6
# teaching_table_area = circle.area(36 / 2) # diameter == 36
# round_room_area = circle.area(11460 / 2) # diameter == 11460

# print(round_room_area)

# **************************** Constructors ****************************

# Constructors are methods used to prepare the instantiated objects (__init__())

class Circle():

	def __init__(self, diameter): # constructor specifies that a circle when created the diameter must be given
		
		print("New circle with diameter: {diameter}".format(diameter=diameter))

#teaching_table = Circle(36)

# **************************** Instances Variables ****************************

class Store():

	pass 

alternative_rocks = Store() # first instance
isabelles_ices = Store() # second instance

alternative_rocks.store_name = "Alternative Rocks" # give and attribute for the first instance
isabelles_ices.store_name = "Isabelle's Ice" # give and attribute for the second instance

#print(alternative_rocks.store_name)

# print(hasattr(alternative_rocks, 'store_name')) # True if the instance has the attribute store_name
# print(getattr(alternative_rocks, 'store_name', 800)) # Get the value of the attribute, returns 800 if there is not attribute

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

# check if the element has the attribute count using the hasattr() function. If so, print the following line of code: 

# for element in can_we_count_it:

# 	if hasattr(element, 'count'):

# 		print("The %s element is %s type and it has the count attribute. \
# 			" %(str(element), str(type(element))))

# 	else:
# 		print("The %s element is %s type and it does not have the count attribute. \
# 			" %(str(element), str(type(element))))

# **************************** Self ****************************

# The constructor can be used to create the instances, through the parameters provided.

class Circle:
	pi = 3.14
	def __init__(self, diameter):
		# print("Creating circle with diameter {d}".format(d=diameter))
		
		# Add assignment for self.radius here:
		self.radius = diameter / 2
	
	# the method __repr__() is used to print the string representation of an object

	def __repr__(self):

		return('Circle with radius {r}'.format(r=self.radius))

	# define new method to calculate circumference length

	def circumference(self):
		length = 2 * self.pi * self.radius
		return length

# define three circles with three different diameters

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# print out the three circumferences

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

print(medium_pizza) # prints the string representation of the instance
print(teaching_table)
print(round_room)









