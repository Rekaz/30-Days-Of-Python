import math
t = tuple()
print (t)

tb = ('a','b','c')
ts = ('a','b','c')

tsib = tb + ts
print (tsib)

print (len(tsib))

lst = list (tsib)
lst.append ("m")
lst.append ("f")
tup = tuple (lst)
print (tup)

par = tup[-2:]
print (par)
sib = tup [:-2]
print (sib)

f = ('a','b','c')
v = ('x','a')
ap = ('m','a','b','x')
fp = f + v + ap
print (fp)

fpl = list (fp)
print (fpl)

mid = len (fpl)/2
if len (fpl)%2:
    mid = math.floor (len (fpl)/2)    
    m1 = fpl [mid]
    m2 = fpl [mid+1]
    m = m1+m2
else:
    mid = len (fpl)/2
    m = fpl [mid]    
print (m)

f3 = fpl [0:3]
print (f3)
l3 = fpl [-3:]
print (l3)

del fp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print ('Estonia' in nordic_countries)
print ('Iceland' in nordic_countries)