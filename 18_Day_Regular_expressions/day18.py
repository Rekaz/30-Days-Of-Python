import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
lst = []
paragraph = paragraph.replace('.',"")
print (paragraph)
regex = re.split(' ', paragraph)
print (regex)
for word in regex:
    print (word)
    # if 
    lst.append (tuple(re.findall(word,paragraph)))
print (lst)
lst2 = []
for index,word in enumerate(lst): 
    c = 1
    for j in lst[index]:
        c+=1
    tup = (c,lst[index][0])
    lst2.append(tup)
print (lst2)
st = set (lst2)
print (st)