import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.countries_data import cd
from data.countries import countries

for i in range(11):
    print (i)
i = 0
while i != 11:
    print (i)
    i +=1

for i in range (-1,10,-1):
    print (i)

i = 10
while i != 0:
    print (i)
    i -=1

i = 1
while i <= 7:
    print (i*"#")
    i+=1

i = 1
while i <=8:
    print (8*"# ")
    i +=1


for i in range (11):
    print (f"{i} x {i} = {i*i}")

data = ['Python', 'Numpy','Pandas','Django', 'Flask']
for d in data:
    print (d)

for i in range (0,101,2):
    print (i)

for i in range (1,101,2):
    print (i)
sum = 0    
for i in range (0,101):
   sum +=i
print (sum)
sumeven, sumodd = 0,0
for i in range (0,101):
    if i%2==0:
        sumeven +=i
    else:
        sumodd +=i 
print (sumeven)
print (sumodd)

for c in countries:
    if 'land' in c:
        print (c)
    else:
        continue
             
fruit = ['banana', 'orange', 'mango', 'lemon']
for f in fruit:
    f_rev = fruit[::-1]
print (f_rev)

c = 0
lan = []
for m in cd:
    c +=len(m["languages"])
    lan += m["languages"]
t={}
for l in lan:
    t[l] = 1 + t.get(l,0)
lst = t.keys()
print (len(lst))
# print (t.items())
sort_lan = dict(sorted (t.items(), key=lambda item: item[1],reverse=True))
for i, key in enumerate(sort_lan.keys()):
    if i == 11:
        break
    print (key)
t = {}
for p in cd:
    t[p["name"]] = p["population"]
sorted_data = dict (sorted(t.items(), key=lambda item: item[1],reverse=True))
for i, key in enumerate (sorted_data.keys()):
    if i ==11:
        break
    print (key)

    