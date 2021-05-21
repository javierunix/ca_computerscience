letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Using a list comprehension and zip, create a dictionary called letter_to_points
letter_to_points = {}

for (k, v) in zip(letters, points):
    letter_to_points[k] = v


# Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points[" "] = 0
# print(letter_to_points)

# Define a function called score_word that takes in a parameter word.

def score_word(word):
    point_total = 0 # create a variable and set it to 0
    for i in range(len(word)):
        if word[i] in letter_to_points.keys():
            point_total += letter_to_points[word[i]]
    return point_total

brownie_score = score_word("BROWNIE")
# print(brownie_score)

# Create a dictionary called player_to_words that maps players to a list of the words they have played.
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], \
    "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"],\
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# create and empty dict called player_to_points
player_to_points = {}

# Iterate through the items in player_to_words. Call each player player and each list of words words.
# Within your loop, create a variable called player_points and set it to 0.

for player, words in player_to_words.items(): # loop over the dictionary
    player_points = 0 # for every player create a variable to store the points and initialize to 0
    for word in words: # iterate over the words of the player
        player_points += score_word(word) # call the function for the word and increase the puntuation
    player_to_points[player] = player_points # player as key and punctuation as value
print(player_to_points)