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
		self.items = items
		self.start_time = start_time
		self.end_time = end_time

	def __repr__(self):
		return("%s available from %d to %d." %(self.name, self.start_time, self.end_time))

	def calculate_bill(self, purchased_items): # parameters: self and a list with items
		total_sum = 0 # initialize total_sum
		for item in purchased_items: # iterate over items list
			total_sum += self.items[item] # add the value of the item to the sum according to the items dictionary
		return total_sum

# create first menu
brunch = Menu('brunch menu', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

# create second menu

early_bird = Menu('early bird menu', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

# create third menu
dinner = Menu('dinner menu', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

# create kids menu

kids = Menu('kids menu', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# let’s create a Franchise class.

# Give Franchise an .available_menus() method that takes in a time parameter 
# and returns a list of the Menu objects that are available at that time.
class Franchise():

	def __init__(self, address, menus):
		self.address = address
		self.menus = menus

	def __repr__(self):
		return("our address is %s" %self.address)

	def available_menus(self, time):
		list_available_menus = [] # initialize the list
		for menu in self.menus: # iterate over the menus list
			if menu.end_time >= time >= menu.start_time: # if time specified is between start and end
				list_available_menus.append(menu.name) # add to the list the name of the menu
		return list_available_menus
			
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# print(flagship_store)
# print(new_installment)
# print(flagship_store.available_menus(12))
# print(flagship_store.available_menus(17))

# define a Bussiness class

class Bussiness():

	def __init__(self, name, franchises):
		self.name = name
		self.franchises = franchises

# create a new menu
arepas_menu = Menu('arepas menu', {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)

# create a new Franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [brunch, early_bird, dinner, kids, arepas_menu])
#print(arepas_place)

# create a bussiness instance
new_bussiness = Bussiness("Take a' Arepa", [flagship_store, new_installment, arepas_place])

