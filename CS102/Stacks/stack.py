import node

# create Stack class
class Stack:
    def __init__(self, limit = 1000):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def push(self, value):
        if self.has_space():
            item = node.Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            print("Adding {} to the pizza stack!".format(value))
            self.size += 1
        else:
            return("All out of space!")

    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = self.top_item.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            return("Sorry, the Stack is totally empty :-(")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        else:
            return("Nothing to see here!")

    def has_space(self):
        if self.limit > self.size:
            return True
        else:
            return False

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
print(pizza_stack.pop())
print(pizza_stack.pop())
print(pizza_stack.pop())
print(pizza_stack.pop())
print(pizza_stack.pop())
print(pizza_stack.pop())

# Uncomment the pop() statement below:
print(pizza_stack.pop())
