# Observatios:
# A namespace is a collection of defined symbolic names along with information
# about the object that the name references.

class Facade: # Define a class with the 'class' keyword. It is recommended capitalize the class name
	pass

# Make a Facade instance and save it to the variable facade_1

facade_1 = Facade()

# try calling type() on facade_1 and saving it to the variable facade_1_type
facade_1_type = type(facade_1)

# print(facade_1_type) # output: <class '__main__.Facade'>

# Create a Grade class with a class attribute minimum_passing equal to 65.
class Grade:
	minimum_passing = 65

# Create a Rules class so that we can explain the rules.
# Give Rules a method washing_brushes that returns a string.

class Rules:
	def washing_brushes(self): # self refers to the object calling the function.
		return("Point bristles towards the basing while washing your brushes.")

# create a Circle class with variable pi = 3.14

class Circle:

	pi = 3.14

	def get_area(self, radius): # method given to class circle
		area = self.pi * radius ** 2
		return(area)

circle = Circle() # create and instance of class Circle

# calculate the area of...

# a pizza 12 inches across
pizza_area = circle.get_area(12 / 2)

# a teaching table 36 inches across
teaching_area_table = circle.get_area(36 / 2)

# the Round Room auditorium (11460 inches across)
round_room_table = circle.get_area(11460 / 2)

print(pizza_area)
print(teaching_area_table)
print(round_room_table)


