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

