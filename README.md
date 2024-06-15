# School Catalogue

The School Catalogue project implements a digital catalog for schools under the New York City Department of Education. It utilizes object-oriented programming principles in Python to manage different types of schools and their properties.

## Classes

### School

The `School` class serves as the parent class for all types of schools and includes the following features:

- **Properties**:
  - `name` (string): The name of the school.
  - `level` (string): The level of the school ('primary', 'middle', or 'high').
  - `numberOfStudents` (integer): The number of students enrolled.

- **Methods**:
  - `__init__(name, level, numberOfStudents)`: Initializes the school with the given parameters.
  - `__repr__()`: Provides a string representation of the school object.
  - `get_name()`: Returns the name of the school.
  - `get_level()`: Returns the level of the school.
  - `get_numberOfStudents()`: Returns the number of students.
  - `set_numberOfStudents(numberOfStudents)`: Sets the number of students.

### PrimarySchool

The `PrimarySchool` class inherits from `School` and adds the following feature:

- **Properties**:
  - `pickupPolicy` (string): Specifies the pickup policy for students.

- **Methods**:
  - `__init__(name, numberOfStudents, pickupPolicy)`: Initializes a primary school with the given parameters.
  - `__repr__()`: Provides a string representation of the primary school object.
  - `get_pickupPolicy()`: Returns the pickup policy of the primary school.

### HighSchool

The `HighSchool` class inherits from `School` and adds the following feature:

- **Properties**:
  - `sportsTeams` (list of strings): Lists the sports teams available at the school.

- **Methods**:
  - `__init__(name, numberOfStudents, sportsTeams)`: Initializes a high school with the given parameters.
  - `__repr__()`: Provides a string representation of the high school object.
  - `get_sportsTeams()`: Returns the list of sports teams at the high school.

## Usage

To use this catalog, instantiate objects of the respective classes (`School`, `PrimarySchool`, `HighSchool`) with appropriate properties and access their methods as demonstrated below:

```python
# Creating instances of schools
test1 = School("Wood", "down", 40)
print(test1)

print(test1.get_name())
print(test1.get_level())
print(test1.get_numberOfStudents())

test1.set_numberOfStudents(60)
print(test1.get_numberOfStudents())

test2 = PrimarySchool("Madison", 36, "parent")
print(test2)

print(test2.get_name())
print(test2.get_level())
print(test2.get_numberOfStudents())
print(test2.get_pickupPolicy())

test2.set_numberOfStudents(56)
print(test2.get_numberOfStudents())

test3 = HighSchool("Texas", 500, ["football", "soccer"])
print(test3)

print(test3.get_name())
print(test3.get_level())
print(test3.get_numberOfStudents())
print(test3.get_sportsTeams())

test3.set_numberOfStudents(800)
print(test3.get_numberOfStudents())
