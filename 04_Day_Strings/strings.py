tdop = "Thirty " + "Days " + "Of " + "Python"
print (tdop)

cfa = "Coding " + "For " + "All"
print (cfa)

company = "Coding For All"
print (company)
print (len(company))

print (company.upper())

print (company.lower())

print (company.capitalize())
print (company.title())
print (company.swapcase())
 
first_word = company[0:6]
print (first_word)

print (company)
print (company.find('Coding'))
print (company.index('Coding'))


print (company.replace('Coding', 'python'))

var = "python for everyone"
print (var.replace('everyone','all'))

st = 'coding for all'
print (st.split(' '))

st = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print (st.split(','))

print (company[0])

print (len(company)-1)

print (company[10])

pfe = 'Python For Everyone'
cfa =  'Coding For All'

print (cfa.index('C'))

print (cfa.index('F'))

print (cfa.rfind('I'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print (sentence.index('because'))


sentence = 'You cannot end a sentence with because because because is a conjunction'
print (sentence.rindex('because'))


sentence = 'You cannot end a sentence with because because because is a conjunction'
print (sentence.split('because because because'))


sentence = 'You cannot end a sentence with because because because is a conjunction'
print (sentence.index('because'))

print (cfa.startswith('Coding'))

print (cfa.endswith('Coding'))


cfa = '   Coding For All      ' 

l1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print ('# '.join(l1))

sentence = '''I am enjoying this challenge.\nI just wonder what is next.'''

print (sentence.split('\n'))


print ('Name\tAge\tCountry\tCity')
print ('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print (f'The area of a circle with radius {radius} is {area} meters square.')

a=8
b=6

print (f'{a}+{b}={a+b}')
print (f'{a}-{b}={a-b}')
print (f'{a}*{b}={a*b}')
print (f'{a}/{b}={a/b:.2f}')
print (f'{a}%{b}={a%b}')
print (f'{a}//{b}={a//b}')
print (f'{a}**{b}={a**b}')
