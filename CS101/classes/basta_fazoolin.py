# create a Menu class
# give Menu a constructor with the five parameters self, name, items, start_time, and end_time.

# Give our Menu class a string representation method that will tell you the name of the menu. 
# Also, indicate in this representation when the menu is available.

# Give Menu a method .calculate_bill() that has two parameters: 
# self, and purchased_items, a list of the names of purchased items.
# Have calculate_bill return the total price of a purchase consisiting of all the items in purchased_items.

class Menu():

	def __init__(self, name, items, start_time, end_time):
		self.name = name
		self.items =items
		self.start_time = start_time
		self.end_time = end_time

	def __repr__(self):
		return("%s available from %s to %s." %(self.name, self.start_time, self.end_time))

	def calculate_bill(self, purchased_items): # parameters: self and a list with items
		total_sum = 0 # initialize total_sum
		for item in purchased_items: # iterate over items list
			total_sum += self.items[item] # add the value of the item to the sum according to the items dictionary
		return total_sum

# create first menu
brunch = Menu('brunch menu', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, '11 am', '4 pm')

# create second menu

early_bird = Menu('early bird menu', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, '3 pm', '6 pm')

# create third menu
dinner = Menu('dinner menu', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, '5 pm', '11 pm')

# create kids menu

kids = Menu('kids menu', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, '11 am', '9 pm')

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
