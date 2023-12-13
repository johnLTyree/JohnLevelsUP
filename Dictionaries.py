emails = {
            'Anne Stahl' : 'astahl@gmail.com', 
            'Peter Small': 'peters@yandex.com', 
            'Mark Steel': 'Mark@steel.com'
    
        }
print(emails['Mark Steel'])

spanish_animals = {
                   'dog': 'el perro', 
                   'cat': 'el gato', 
                   'horse': 'el caballo', 
                   'bird': 'el pajaro'
                   }
print(spanish_animals['bird'])


grades = {}

grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)

grades['Anne'] = 'A'
print(grades)

grades.update({'John': 'A'})
print(grades)

len(grades)

if 'John' in grades:
    print('John got:', grades['John'])
    
del grades['John']
print(grades)

for el in grades:
    print(el)
    
for el in grades.keys(): 
    print(el)
    
for el in grades.values():
    print(el)
    
for person, grade in grades.items():
    print(person, 'got', grade)
