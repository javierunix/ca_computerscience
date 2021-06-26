from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# landmark_string is a variable that joins all the landmarks together
landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += "{0} - {1}\n".format(letter, landmark)

stations_under_construction = ["Burrard", "Patterson"]

# function with a greetings text for the user:
def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

# the function 'skyroute' contains the full program
def skyroute():
    greet()
    new_route()
    goodbye()

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
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_start()

# To request and end from the user 
def get_end():
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
    if end_point_letter in landmark_choices:
        end_point= landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_end()

def new_route(start_point = None, end_point = None):
    start_point, end_point = set_start_and_end(start_point, end_point)

    shortest_route = get_route(start_point, end_point)

    if shortest_route:
        shortest_route_string = '\n'.join(shortest_route)
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    
    else: 
        print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))

    again = input("Would you like to see another route? Enter y/n: ")

    show_landmarks()

    if again == "y":
        new_route(start_point, end_point)

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]

    routes = [] # empty list to collect the shortest routes

    for start_station in start_stations:

        for end_station in end_stations:
            route = bfs(vc_metro, start_station, end_station)

            if route:
                routes.append(route)

    shortest_route = min(routes, key=len)

    return shortest_route

def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")

    if see_landmarks == "y":
        print(landmark_string)

def goodbye():
    print("Thanks for using SkyRoute!")

def get_active_stations():
    updated_metro = vc_metro

    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])

    return updated_metro