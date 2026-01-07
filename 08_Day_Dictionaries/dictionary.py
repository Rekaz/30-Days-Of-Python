dog = {}
dog['name'] = 'Tom'
dog['color'] = 'Black'
dog['breed'] = 'German Shephard'
dog['legs'] = 4
dog['age'] = 12
print (dog)

student = {'first_name':'John', 'last_name': 'Doe', 'gender':'Male', 'age': 23, 'marital status':'Unmarried', 'skills':["C++","Java"], 'country':'China', 'city': 'Tokyo', 'address':'Tokyo Street'}
print (f"length of student: {len(student)}")

print (f"value of skills: {student.get('skills')}")
print (type(student.get('skills')))
student['skills'].append('HTML')
print (student['skills'])

print (f"Keys as list: {student.keys()}")
print (f"Values as list: {student.values()}")
print (f"Dictionary as list of tuples: {student.items()} ")

del student['age']
del student