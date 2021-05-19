# this is an exercise for mastering lists

subjects = ["physics", "calculus", "poetry", "history"] # create a list with classes taken
grades = [98, 97, 85, 88] # create a list with scores

# create a two-dimensional lists that combines the two previous list
gradebook = [] # create new empty list
for i in range(len(subjects)):  # iterarate over the previous list
    gradebook.append([subjects[i], grades[i]]) # in every iteration append to the new list the i elements of previous list

subject1 = ["computer science", 100] # new list
gradebook.append(subject1) # append new list to gradebook

subject2 = ["visual arts", 93] # new list
gradebook.append(subject2) # append new list to gradebook

# increment in 5 points the grade of visual arts
gradebook[5][1]+= 5

# remove the numerical value for poetry 
gradebook[2].remove(gradebook[2][1]) # remove the second element from the poetry sublist 
gradebook[2].append("Pass") # add Pass to poetry sublist

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create a new variable full_gradebook that combines both 
# last_semester_gradebook and gradebook using + to have one complete grade book.
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

