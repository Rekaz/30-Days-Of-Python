# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print (len(it_companies))
it_companies.add("twitter")
print (f"it companies after adding twitter: {it_companies}")
it_companies.update (["Nvidia","DeepSeek","openAI"])
print (f"it_companies after adding multiple companies {it_companies}")
it_companies.remove ('Facebook')
print ("remove throws error if element not found, but discard doesn't throw any errors")
it_companies.discard ('Facebook')

C = A.union(B)
print (f"Join A and B: {C}")
C = A.intersection(B)
print (f"A intersection B: {C}")
print (f"Is A subset of B: {A.issubset(B)}")
print (f"Are A and B disjoint sets: {A.isdisjoint(B)}")
print (f"Join A with B: {B.union(A)}")
print (f"Join B with A: {A.union(B)}")
print (f"symmetric difference between A and B: {A.symmetric_difference(B)}")
del A
del B
del it_companies

st =set (age)
print (f"length of list: {age}")
print (f"length of set: {st}")
if len(age) > len(st):
    print (f"bigger one is list")
else:
    print ("bigger one is set")

print ("string: any text , list: mutable, indexed, ordered, allow duplicates; tuple: immutable, indexed,ordered, allow duplicates;set:,immutable, unordered, unindexed, distinct (no duplicates)")

text = "I am a teacher and I love to inspire and teach people"
words = text.split()
print (words)
text_set = set (words)
print (text_set)
print (f"Number of unique words in text: {text} are = {len(text_set)}")

