# this is an exercise for mastering lists

subjects = ["physics", "calculus", "poetry", "history"] # create a list with classes taken
grades = [98, 97, 85, 88] # create a list with scores

# create a two-dimensional lists that combines the two previous list
gradebook = {}
i = 0
for item in subjects:
    gradebook[item] = grades[i]
    i+=1
print(gradebook)
