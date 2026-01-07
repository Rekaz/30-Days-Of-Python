dog ={}
# dog = {"name":"d","color":"c","breed":"b","age":250}
dog["name"]="d"
dog["color"]="c"
dog["breed"] = "b"
dog["age"] = 250
student = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'gender':'male',
    'country':'Finland',
    'city':'den',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print (len(student))
print (student.values())
print (type(student["skills"])==list)
student["skills"].append('adfdf')
student["skills"].append('adfdfsfd')
print (list(student.keys()))
print (list(student.values()))
print (list(tuple(student.items())))

dog.pop("breed")
print (dog)
del dog