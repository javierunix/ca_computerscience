"""
The Magic 8-Ball is a popular toy 
developed in the 1950s for fortune-telling or advice seeking.
Write a magic8.py Python program that can answer any “Yes” or “No” question 
with a different fortune each time it executes.

We’ll be using the following 9 possible answers for our Magic 8-Ball
"""

#               ******* Setting up *********

# Step 1 
# In magic_8_ball.py, declare a variable name and assign it to the name of the person
# who will be asking the Magic 8-Ball.
# name = "Noa"

#Step 2
# Next, declare a variable question, and assign to a “Yes” or “No” 
# question you’d like to ask the Magic 8-Ball.
# question = "do you like napolitan pizza?"

# Step 3
#We want to store the answer of the Magic 8-Ball in another variable, 
# which we’ll call answer. 
#For now, assign this variable to an empty string.
answer = ""

#               ******* Generating a random number *********


# Step 4
import random 

# Step 5
# create a variable to store the randomly generated value.
random_number = random.randint(1, 9) # generate a random integer, between 1 and 9 (inclusive)


#               ******* Control Flow *********

# Steps 6-8
# we use if/elif/else staments to associate every possible integer generated with a specific answer

if random_number == 1:
    answer = "yes - definitely"
elif random_number == 2:
    answer = "it is decidedly so."
elif random_number == 3:
    answer = "without a doubt."
elif random_number == 4:
    answer = "reply hazy, try again."
elif random_number == 5:
    answer = "ask again later."
elif random_number == 6:
    answer = "better not to tell you now."
elif random_number == 7:
    answer = "my sources say no."
elif random_number == 8:
    answer = "outlook not so good."
elif random_number == 9:
    answer = "very doubtful."
else: 
	answer = "error"


#               ******* Seeing the result *********


# Step 9
# print() statement to output the asker’s name and their question 
# with the format [Name] asks: [Question]

# print("%s asks %s" %(name, question))

# Step 10
# Add a second print() statement that will output the Magic 8-Ball’s answer in the following format:
# Magic 8-Ball's answer: [answer]

# print("Magic 8-Ball's answer: %s" %answer)

# step 13
# What if the asker does not provide a name, 
# such that the value of name is an empty string? 
# If the name string is empty, the output of the program looks like the following:
# asks: Will I win the lottery? Magic 8 Ball's answer: Outlook not so good

name = "Nerea"

# if name == "":
#     print("Will I win the lottery?")
# else: 
#     print("%s asks %s" %(name, question))

# print("Magic 8-Ball's answer: %s" %answer)

# What if the question string is empty? 
# If the user does not provide any question, 
# then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!

question = "do you like napolitan pizza?"
if question == "":
    print("Hey, user, you have to privide a question")
else:
    if name == "":
        print("Will I win the lottery?")
    else: 
        print("%s asks %s" %(name, question))
        print("Magic 8-Ball's answer: %s" %answer)


