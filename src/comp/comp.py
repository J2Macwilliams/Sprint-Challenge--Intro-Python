# The following list comprehension exercises will make use of the 
# defined Human class. 
"""
--Assumptions:
    -- Must abstract name and from class instance
    --Must use values to create list comprehension
"""
import string

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]
# access names and ages
# loop thru list to grab names and ages
# assign names to variable
# assign ages to variables
# for person in humans:
#     name = person.name
#     age = person.age

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [person.name for person in humans if person.name.startswith('D')]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [person.name for person in humans if person.name.endswith('e')]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

letters= list(string.ascii_lowercase[2:7])
print(letters)
print("Starts between C and G, inclusive:")
c = []
for l in letters:
    people = [person.name for person in humans if person.name.lower().startswith(l)]
    c.extend(people)
    
print(c)


# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [person.age + 10 for person in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [person.name + "-"+ str(person.age) for person in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.

print("Names and ages between 27 and 32:")

f = [(person.name, person.age) for person in humans if person.age > 26 and person.age < 33]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [person.name.upper() for person in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(person.age) for person in humans]
print(h)
