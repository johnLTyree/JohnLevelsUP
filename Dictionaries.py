# Dictionary of emails
emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'peters@yandex.com',
    'Mark Steel': 'Mark@steel.com'
}

# Access and print the email for 'Mark Steel'
print(emails['Mark Steel'])

# Dictionary of Spanish animal names
spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pajaro'
}

# Access and print the Spanish name for 'bird'
print(spanish_animals['bird'])

# Empty dictionary for grades
grades = {}

# Add grades for students
grades['John'] = 'A-'
grades['Anne'] = 'B'

# Print the current grades
print(grades)

# Update Anne's grade
grades['Anne'] = 'A'

# Print the updated grades
print(grades)

# Update John's grade using the update method
grades.update({'John': 'A'})

# Print the updated grades
print(grades)

# Get the number of items in the grades dictionary
print(len(grades))

# Check if 'John' is in the grades dictionary and print his grade
if 'John' in grades:
    print('John got:', grades['John'])

# Delete John's grade
del grades['John']

# Print the grades after deleting John's entry
print(grades)

# Iterate through keys in the grades dictionary and print them
for el in grades:
    print(el)

# Alternatively, iterate through keys using the keys() method
for el in grades.keys():
    print(el)

# Iterate through values in the grades dictionary and print them
for el in grades.values():
    print(el)

# Iterate through both keys and values and print them
for person, grade in grades.items():
    print(person, 'got', grade)
