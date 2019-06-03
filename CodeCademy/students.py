class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []


  def add_grade(self, grade):
    self.grade = grade
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      pass

#  def get_scores(self):
#    for x in self.grades:
#      return [x]

  def get_average(self):
   # scores = [score.score for score in self.grades]
   suma = 0
   for grade in self.grades:
       suma += grade.score
   return suma / len(self.grades)

class Grade:
  def __init__(self, score):
    self.score = score

  def __repr__(self):
    return str(self.score)

  minimum_passing = 65

  def is_passing(self):
    if self.score >= self.minimum_passing:
      return True
    else:
      return False

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(8))
pieter.add_grade(90)
print(pieter.grades)
for grade in pieter.grades:
  print(grade.is_passing())
  print(grade)
print(pieter.get_average())
