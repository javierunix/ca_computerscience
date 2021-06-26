from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# landmark_string is a variable that joins all the landmarks together
landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += "{0} - {1}\n".format(letter, landmark)

# function with a greetings text for the user:
def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

# the function 'skyroute' contains the full program
def skyroute():
    greet()

# This function handles the selected origin and destination
def set_start_and_end(start_point, end_point):
    if start_point is not None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")

        if change_point == "b":
            start_point = get_start()
            end_point = get_end()

        elif change_point == "o":
            start_point = get_start()

        elif change_point == "d":
            end_point = get_end()
        
        else:
            print("Oops, that isn't 'o', 'd', or 'b'...")
            set_start_and_end(start_point, end_point) 

    else:
        start_point = get_start()
        end_point = get_end()

    return start_point, end_point
# To request and origin from the user 
def get_start():
    pass

# To request and end from the user 
def get_end():
    pass