load_file_in_context("queue.py")

try:
  q = Queue()
  q.head = Queue(9)
  if q.peek() != 9:
    fail_tests("Did you return `self.head.get_value()` within your `peek()` method?")
except AttributeError:
  fail_tests("Did you define a method `peek()` for `Queue`?")
except TypeError as e:
  fail_tests(e)
  #fail_tests("Did you define a method `peek()` with `self` as a paramenter?")

pass_tests()