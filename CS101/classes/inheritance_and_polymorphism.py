class Bin:
	pass

# Create a subclass of Bin

class RecyclingBin(Bin):
	pass 

# ********************** Inheritance from Exception Class ********************* 

# 1. Define our own exception called OutOfStock that inherits from the Exception class.

class OutOfStock(Exception):
  """
  Exception for when there are not candles to sell.
  """
class CandleShop:

  name = "Here's a Hot Tip: Buy Drip Candles"

  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):

    if self.stock[color] < 1: # if there are not candles, raise exception
      raise OutOfStock

    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 1})
candle_shop.buy('blue')

# This should raise OutOfStock:
candle_shop.buy('green')

# ********************** Overriding Methods *********************

# 1. We’ve defined two classes, Message and User 

# 2. Create an Admin class that subclasses the User class.

class Message:

  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:

  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

class Admin(User):

  def edit_message(self, message, new_text):
    message.text = new_text

# ********************** Super() *********************
# super() gives a proxy object, that allows to invoke the method of the object's parent class.

class PotatoSalad:

  def __init__(self, potatoes, celery, onions):

    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

class SpecialPotatoSalad(PotatoSalad): 

  def __init__(self, potatoes, celery, onions, raisins= 40): # SpecialPotatoesSalad takes and aditional argument

    super().__init__(potatoes, celery, onions)  # invoke the parents class for defining three arguments

    self.raisins = raisins # definining the fourth argument

# ********************** Interfaces *********************

# When two classes have the same methods name and the same attributes it is said 
# that these classes implement the same interface.
# In python an interface ussually refers to the names of the methods and the arguments they take.

# 1. Define a clase

class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

# 2. Define a subclass
class VehicleInsurance(InsurancePolicy):
  # Give VehicleInsurance a .get_rate() method that takes self as a parameter. Return .001 multiplied by the price of the vehicle.
  def get_rate(self):
    return 0.001 * self.price_of_insured_item

# 3. Define another subclass
# Give VehicleInsurance a .get_rate() method that takes self as a parameter. Return .00005 multiplied by the price of the vehicle.
class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return 0.00005 * self.price_of_insured_item


# ********************** Polimorphism *********************

# Polymorphism is the term used to describe the same syntax (or method) 
# doing different actions depending on the type of data.

# ******************** Dunder Methods **********************


# Define class Atoms
# Give Atom a .__add__(self, other) method that returns 
# a Molecule with the two Atoms together in a list.

class Atom():

	def __init__(self, label):
		self.label = label

	def __add__(self, other):
		return Molecule([self, other])

# Define classes Molecules
class Molecule():
	def __init__(self, atoms):
		if type(atoms) is list:
			self.atoms = atoms

# Give LawFirm a .__len__() method that will return the number of lawyers in the law firm.
# Give LawFirm a .__contains__() method that takes two parameters: self and lawyer and checks to see if lawyer is in self.lawyers.
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyer):
    return lawyer in self.lawyers
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])