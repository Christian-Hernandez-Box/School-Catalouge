class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents
  
  def set_numberOfStudents(self, numberOfStudents):
    self.numberOfStudents = numberOfStudents

###################################################### 
test1 = School("Wood", "down", 40)
print(test1)

print(test1.get_name())
print(test1.get_level())
print(test1.get_numberOfStudents())

test1.set_numberOfStudents(60)
print(test1.get_numberOfStudents())
######################################################

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, level="primary", numberOfStudents=numberOfStudents)
    self.name = name
    self.numberOfStudents = numberOfStudents
    self.pickupPolicy = pickupPolicy

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students. The pickup policy is {self.pickupPolicy}"

  def get_pickupPolicy(self):
    return self.pickupPolicy
######################################################

test2 = PrimarySchool("Madison", 36, "parent")
print(test2)

print(test2.get_name())
print(test2.get_level())
print(test2.get_numberOfStudents())
print(test2.get_pickupPolicy())

test2.set_numberOfStudents(56)
print(test2.get_numberOfStudents())
######################################################

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, level="high", numberOfStudents=numberOfStudents)
    self.name = name
    self.numberOfStudents = numberOfStudents
    self.sportsTeams = sportsTeams

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students. The sports teams are {self.sportsTeams}"

  def get_sportsTeams(self):
    return self.sportsTeams
######################################################

test3 = HighSchool("Texas", 500, "football & soccer")
print(test3)

print(test3.get_name())
print(test3.get_level())
print(test3.get_numberOfStudents())
print(test3.get_sportsTeams())

test3.set_numberOfStudents(800)
print(test3.get_numberOfStudents())  