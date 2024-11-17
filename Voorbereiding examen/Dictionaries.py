student = {'name': 'John', 'age': 25, 'courses': ['math', 'science']}
print(student['name'])

student['phone'] = '555-5555'
student.update({'name': 'Jane'})

print(student.get('town', 'not found'))
print(student.get('name'))

for key, value in student.items():
    print(key, value)