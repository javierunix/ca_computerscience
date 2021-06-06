from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# create variable stacks a set it to empty list
stacks = []

# create three stacks instances
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

# append the three instances to list "stacks"
for instance in [left_stack, middle_stack, right_stack]:
    stacks.append(instance)

## ********** Set Up the Game ***************

num_disks = int(input("\nHow many disks do you want to play with?\n"))

# ask the player to set a number 3 or more disks
while num_disks < 3:
    num_disks = int(input("Enter a number of disks greater than or equal to 3\n"))

for i in range(num_disks, 0, -1): # iterate backwards over disks
    left_stack.push(i)  # push the number onto the left_stack

num_optimal_moves = 2 ** num_disks - 1
print("The fastest you can solve this game is in %d moves" % num_optimal_moves)

# ************** Define a function for getting user input **************

def get_input():

    choices = [stack.get_name()[0] for stack in stacks] # list with the first letter of each stack: left, middle and right

    while True: # ask the user until we get a valid answer

        for i in range(len(stacks)): # print out the choices
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter %s for %s" %(letter, name))

        user_input = input("")

        if user_input in choices: # if user input is valid, iterate over choices to return the correspondent stack
            for i in range(len(stacks)): 
                if user_input == choices[i]:
                    return stacks[i]


# ************** Playing the Game **************

num_user_moves = 0 

# the game ends when the right stack is full

while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks")

    for stack in stacks:
        print(stack.print_items())

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()


        if from_stack.is_empty(): # if 
            print("\n\nInvalid Move. Try Again")

        # check if move is valid
        # if move to an empty stack o move a disk into a larger one
        elif (to_stack.is_empty()) or (from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break

        else:
            print("\n\nInvalid Move. Try Again")

print("\n\nYou Completed the game in %d, and the optimal number of moves is %d." %(num_user_moves, num_optimal_moves))
