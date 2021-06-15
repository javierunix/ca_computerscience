# user_choice = input("What is your name? ")
# print(user_choice)
# print("Once upon a time...")

######
# TREE NODE CLASS

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
            chosen_index = choice - 1
            chosen_child = story_node.choices[chosen_index]
            print(chosen_child.story_piece)
            story_node = chosen_child

######

######
# VARIABLES FOR TREE


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

choice_a_1_text = """
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
"""

choice_a_2_text = """
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
"""

choice_b_text = """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""

choice_b_1_text = """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
 
YOU REMAIN LOST.
"""

choice_b_2_text = """
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
"""
######

######
# TESTING AREA

story_root = TreeNode(text_1)  # assign to this variable the value text_1
choice_a = TreeNode(choice_a_text)
choice_a_1 = TreeNode(choice_a_1_text)
choice_a_2 = TreeNode(choice_a_2_text)
choice_b = TreeNode(choice_b_text)
choice_b_1 = TreeNode(choice_b_1_text)
choice_b_2 = TreeNode(choice_b_2_text)

print(story_root.story_piece)

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

# print(story_root.choices)

story_root.traverse()
######
