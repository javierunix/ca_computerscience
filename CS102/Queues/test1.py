load_file_in_context("main.py")

try:
  Queue
  if type(Queue) != type:
    fail_tests("Did you make `Queue` a class?")
  q = Queue()
except NameError:
  fail_tests("Did you define a class called `Queue`?")
except TypeError:
  fail_tests("Did you give `Queue` an `__init__()` method with `self` as a parameter?")

try:
  if q.head != None:
    fail_tests("Did you assign `self.head` to `None` within `Queue`'s `__init__()` method?")
  elif q.tail != None:
    fail_tests("Did you assign `self.tail` to `None` within `Queue`'s `__init__()` method?")
except NameError:
  fail_tests("Did you add `head` and `tail` as attributes within `__init__()`?")
except AttributeError:
  fail_tests("Did you create an `__init__()` method with `self.head` and `self.tail` as attributes?")
  
pass_tests()