import math
a = int (input ("enter your age:"))
if a >=18:
    print ("old")
else:
    print ("Wait")
ma = int (input ("Enter your age: "))
my = int (input ("my age: "))
if ma == my:
    print ("equal")
elif ma -my==1 or my -ma ==1:
    print ("! year gap")
else:
    print ("years")

a = int (input ("A"))
b = int (input ("B"))
if a < b:
    print (f"{b} is greater than {a}")
elif a>b:
    print (f"{a} is greater than {b}")
else:
    print (f"{a} is equal to {b}")

sc = int (input ("enter grade:"))
if sc >=80 and sc < 100:
    print ("A")
elif sc >=70 and sc <=79:
    print ("B")
elif sc >=60 and sc <=69:
    print ("C")
elif sc >= 50 and sc <= 59:
    print ("D")
else:
    print ("F")

m = input ("enter month:")
if m == "September" or m == "October" or m == "November":
    print ("Autumn")
elif m == "December" or m == "January" or m == "February":
    print ("Winter")
elif m == "March" or m == "April" or m == "May":
    print ("Spring")
elif m == "June" or m == "July" or m == "August":
    print ("Summer")
else:
    print ("enter a valid month")
    
fruits = ['banana', 'orange', 'mango', 'lemon']
f = input ("enter fruit: ")
if f in fruits:
    print ("That fruit already exist in the list")
else:
    fruits.append(f)
    print (f"{fruits}")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if person.get('skills'):
    a = math.ceil(len(person["skills"]) /2)
if person.get ('skills') and 'Python' in person["skills"]:
     print ("true")
else:
    print ("false")
if 'JavaScript' in person["skills"] and 'React' in person["skills"]:
    print ("front end developer")
elif 'Node' in person["skills"] and 'Python' in person["skills"] and 'MongoDB' in person["skills"]:
    print ("backend developer")
elif 'Node' in person["skills"] and 'React' in person["skills"] and 'MongoDB' in person["skills"]:
    print ("full stack developer")
else:
    print ("unknown")
if person["is_marred"] == True and person["country"] == 'Finland':
    print (f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
    
