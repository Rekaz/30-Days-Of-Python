# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print (len (it_companies))
it_companies.add('twitter')
print (it_companies)

it_companies.update('z','a','y')
print (it_companies)

it_companies.remove('z')

print ("for remove, it must be a member of set, otherwise keyerror, unlike discard, it does nothing if not the member")

A.union(B)
print (A)
print (A.intersection(B))
print (A.issubset(B))
print (A.isdisjoint(B))
print (B.isdisjoint(A))
print (A.union(B))
print (B.union(A))
print (A.symmetric_difference(B))
A.clear()
B.clear()
it_companies.clear()

st = set (age)
if len(st) < len (age):
    print ("list")
else: 
    print ("set")

s = "I am a teacher and I love to inspire and teach people"
l = s.split(' ')
s= set (l)
print (s)
print (len(s))
