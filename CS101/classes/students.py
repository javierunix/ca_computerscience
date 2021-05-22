# define the class student

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade: # if grade belongs to the class Grade is appended to the list
      self.grades.append(grade)
  
  def get_average(self): 
  	total = 0
  	for grade in self.grades: # loop through the list of grades
  		total += grade.score # extract the numerical equivalent of the grade to increase the sum
  	return total / len(self.grades)

# define the class Grade
class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(80))


# for item in pieter.grades:
# 	print(item.score)   # we have to extract the score value to print the grade

# print(pieter.get_average())