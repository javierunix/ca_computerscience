# user_choice = input("What is your name? ")
# print(user_choice)
#print("Once upon a time...")

######
# TREENODE CLASS
######

# Our TreeNode class will keep track of two things:
# 1. a portion of the story
# 2. the choices that the user does in order to progress the story
class TreeNode:

    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        while len(story_node.choices) > 0:
            choice = int(input("Enter 1 or 2 to continue the story: "))
            while choice not in [1, 2]:
                choice = int(input("Enter a valid choice 1 or 2: "))
            story_node.add_child(choice)
            story_node.choices.pop()



text_1 = """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""

choice_a_text = """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""


choice_b_text = """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""

story_root = TreeNode(text_1) # assign to this variable the value text_1
choice_a = TreeNode(choice_a_text)
choice_b = TreeNode(choice_b_text)

#print(story_root.story_piece)

story_root.add_child(choice_a)
story_root.add_child(choice_b)
#print(story_root.choices)

story_root.traverse()


