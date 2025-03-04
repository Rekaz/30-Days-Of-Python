age = input ("Enter your age: ")
if int(age) >= 18:
    print ("You are old enough to drive.")
else: 
    print (f"You need {18-int(age)} more years to learn to drive.")
    
my_age = 40
your_age = input ("This is your age: ")
your_age = int(your_age)
if (my_age == your_age+1):
    print (f"I am 1 year older than you")
elif (my_age+1 == your_age):
    print (f"you are 1 year older than me") 
elif (my_age > your_age+1):
    print (f"I am {my_age-your_age} years older than you ")
elif (my_age + 1 < your_age):
    print (f"you are {your_age-my_age} years older than me ")
else :
    print ("we are equals")

a = input ("Enter number one: ")
b = input ("Enter number two: ")
if a > b:
    print (f"{a} is greater than {b}")
elif b > a:
    print (f"{b} is greater than {a}")
else:
    print (f"{a} is equal to {b}")
    
score = int (input ("Enter your score: "))
if score >= 80 and score <=100:
    print ("Grade A")
elif score >= 70 and score <=79:
    print ("Grade B")
elif score >= 60 and score <=69:
    print ("Grade C")
elif score >= 50 and score <=59:
    print ("Grade D")
elif score >= 0 and score <=49:
    print ("Grade F")
else:
    print ("Invalid score")

month = input ("Enter month: ")
if month == "September" or month == "October" or month == "November":
    print (f"Autumn")
elif month == "December" or month == "January" or month == "February":
    print (f"Winter")
elif month == "March" or month == "April" or month == "May":
    print (f"Spring")
elif month == "June" or month == "July" or month == "August":
    print (f"Summer")
else:
    print ("wrong month")

my_fruit = input ("Enter a fruit name: ")
fruits = ['banana', 'orange', 'mango', 'lemon']
if my_fruit in fruits:
    print ('That fruit already exist in the list')
else:
    fruits.append(my_fruit)
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

if 'skills' in person:
    mid = len(person["skills"])//2
    print (f"{person['skills'][mid]}")
else:
    print ("unskilled person")

if "skills" in person and "Python" in person["skills"]:
    print ("Python is present")
elif "skills" in person and "Python" not in person["skills"]:
    print ("Skills are there but python is not present")
else:
    print ("unskilled person")

if "React" in person["skills"] and "Node" in person["skills"] and "MongoDB" in person["skills"]:
    print ('He is a fullstack developer')
elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
    print ('He is a backend developer')
elif "JavaScript" in person["skills"] and "React" in person["skills"]:
    print ('He is a front end developer')    
else: 
    print ('unknown title')

if person["is_marred"] and person["country"] == "Finland":
    print ("Asabeneh Yetayeh lives in Finland. He is married.")
else:
    pass